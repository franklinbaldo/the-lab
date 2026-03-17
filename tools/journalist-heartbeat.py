#!/usr/bin/env python3
"""Journalist Heartbeat — manage Ed Yong's Jules session against the-lab repo.

Simpler version of rosencrantz-coin's heartbeat.py for a single persona.
Creates/continues a Jules session for the science journalist.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

JULES_API = "https://jules.googleapis.com/v1alpha"
API_KEY = os.environ.get("JULES_API_KEY", "")
SOURCE_NAME = "sources/github/franklinbaldo/the-lab"
SESSION_FILE = Path("journalist/session.json")
SOUL_FILE = Path("journalist/SOUL.md")
SESSION_TTL = timedelta(hours=24)
TITLE_PREFIX = "Journalist — Ed Yong"


def headers():
    return {
        "x-goog-api-key": API_KEY,
        "Content-Type": "application/json",
    }


def now_utc():
    return datetime.now(timezone.utc)


def get_head_sha(short=True):
    fmt = "--short" if short else ""
    r = subprocess.run(
        ["git", "rev-parse"] + ([fmt] if fmt else []) + ["HEAD"],
        capture_output=True, text=True,
    )
    return r.stdout.strip() if r.returncode == 0 else "unknown"


def load_session():
    """Load saved session info."""
    if SESSION_FILE.exists():
        try:
            return json.loads(SESSION_FILE.read_text())
        except Exception:
            pass
    return {}


def save_session(data):
    SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(json.dumps(data, indent=2))


def get_session_info(session_id):
    """Get session state from Jules API."""
    r = requests.get(f"{JULES_API}/sessions/{session_id}", headers=headers())
    if r.status_code != 200:
        return None
    return r.json()


def build_prompt():
    """Assemble the journalist prompt from SOUL.md + recent lab activity."""
    import re as _re
    parts = []

    # Soul
    if SOUL_FILE.exists():
        parts.append(SOUL_FILE.read_text(errors="replace"))

    # Lab state — the primary source of "what's happening"
    state_file = Path("content/state.md")
    if state_file.exists():
        parts.append("\n## Current Lab State (read this first — this is your beat)\n")
        parts.append(state_file.read_text(errors="replace"))
        parts.append("")

    # Recent RFEs (requests for experiments) — emerging debates
    rfes_dir = Path("content/rfes")
    if rfes_dir.exists():
        rfe_files = sorted(rfes_dir.glob("*.md"), reverse=True)[:5]
        if rfe_files:
            parts.append("\n## Recent RFEs (active debates and open questions)\n")
            for r in rfe_files:
                parts.append(f"### {r.name}\n")
                parts.append(r.read_text(errors="replace")[:1000])
                parts.append("")

    # List existing articles — titles only, to avoid duplication
    articles_dir = Path("content/articles")
    covered_titles = []
    if articles_dir.exists():
        article_files = [f for f in sorted(articles_dir.glob("*.md")) if f.name != ".gitkeep"]
        if article_files:
            for a in article_files:
                text = a.read_text(errors="replace")
                title_match = _re.search(r'^title:\s*["\'](.*?)["\']\s*$', text, _re.MULTILINE)
                title = title_match.group(1) if title_match else a.stem
                covered_titles.append(title)
            parts.append("\n## Already Published Articles (topics/angles already taken)\n")
            for t in covered_titles:
                parts.append(f"- {t}")
            parts.append("")

    # Task
    parts.append(
        "\n## Your Task\n"
        "You are a journalist, not a literature reviewer. Your job is NOT to go paper by paper.\n\n"
        "**Start here:** Look at the Recent Lab Activity above. What has happened recently? "
        "What debates are unresolved? What results surprised people? Who disagreed with whom?\n\n"
        "**Find the story:** A good story is a development, a controversy, a turning point — "
        "not a paper summary. The papers are evidence, not the subject.\n\n"
        "**Avoid duplication:** The articles listed above already cover those angles. "
        "Find something those articles did NOT cover — a new development, a new voice, "
        "a shift in the debate, or a result that changes the picture.\n\n"
        "Write 800-1500 words. Save to `content/articles/{slug}.md` with proper frontmatter.\n"
        "If you need to ask a researcher something, use `tools/lab gh issue create`."
    )

    return "\n".join(parts)



def has_open_article_prs():
    """Check if there are already open PRs for articles."""
    r = subprocess.run(
        ["gh", "pr", "list", "--repo", "franklinbaldo/the-lab",
         "--state", "open", "--json", "title,number",
         "--jq", '[.[] | select(.title | test("article|Article|Ed Yong|journalist"; "i"))] | length'],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(f"  WARNING: Could not check open PRs: {r.stderr.strip()}")
        return False
    try:
        count = int(r.stdout.strip())
        if count > 0:
            print(f"  {count} open article PR(s) found — skipping session creation")
            return True
    except ValueError:
        pass
    return False

def create_session():
    """Create a new Jules session for Ed Yong."""
    sha = get_head_sha(short=True)
    ts = now_utc().strftime("%Y-%m-%dT%H:%M")
    title = f"{TITLE_PREFIX} @{sha} {ts}"

    prompt = build_prompt()

    payload = {
        "title": title,
        "prompt": prompt,
        "sourceContext": {
            "source": SOURCE_NAME,
            "githubRepoContext": {"startingBranch": "main"},
        },
        "automationMode": "AUTO_CREATE_PR",
        "requirePlanApproval": False,
    }

    r = requests.post(f"{JULES_API}/sessions", headers=headers(), json=payload)
    if r.status_code != 200:
        print(f"  FAILED to create session: {r.status_code} {r.text[:200]}")
        return None

    data = r.json()
    session_id = data.get("name", "").split("/")[-1]
    print(f"  Created session: {title}")
    print(f"  URL: {data.get('url', 'N/A')}")

    session_data = {
        "session_id": session_id,
        "title": title,
        "created": now_utc().isoformat(),
        "sha": sha,
        "url": data.get("url", ""),
    }
    save_session(session_data)
    return session_id


def send_heartbeat(session_id):
    """Send a heartbeat message to an active session."""
    ts = now_utc().strftime("%Y-%m-%dT%H:%M")
    message = f"Heartbeat {ts} — continue your current work."

    r = requests.post(
        f"{JULES_API}/sessions/{session_id}:sendMessage",
        headers=headers(),
        json={"prompt": message},
    )
    if r.status_code == 200:
        print(f"  Heartbeat sent to session {session_id}")
    else:
        print(f"  Heartbeat failed: {r.status_code}")


def main():
    if not API_KEY:
        print("ERROR: JULES_API_KEY not set")
        sys.exit(1)

    saved = load_session()
    session_id = saved.get("session_id")
    needs_new = False

    if not session_id:
        print("No existing session — creating new")
        needs_new = True
    else:
        info = get_session_info(session_id)
        if not info:
            print(f"Session {session_id} not found — creating new")
            needs_new = True
        elif info.get("state") in ("COMPLETED", "FAILED"):
            print(f"Session {session_id} is {info['state']} — creating new")
            needs_new = True
        else:
            # Check TTL
            created_str = saved.get("created", "")
            if created_str:
                try:
                    created = datetime.fromisoformat(created_str)
                    if now_utc() - created > SESSION_TTL:
                        print(f"Session {session_id} is >24h old — creating new")
                        needs_new = True
                except Exception:
                    pass

            if not needs_new:
                state = info.get("state", "UNKNOWN")
                print(f"Session {session_id} is {state}")
                if state not in ("COMPLETED", "FAILED"):
                    send_heartbeat(session_id)
                return

    if has_open_article_prs():
        print("  Skipping — open article PRs exist. Merge or close them first.")
        return
    create_session()


if __name__ == "__main__":
    main()

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
    """Assemble the journalist prompt from SOUL.md + available content."""
    parts = []

    # Soul
    if SOUL_FILE.exists():
        parts.append(SOUL_FILE.read_text(errors="replace"))

    # List available papers
    papers_dir = Path("content/papers")
    if papers_dir.exists():
        paper_files = sorted(papers_dir.glob("*.md"))
        if paper_files:
            parts.append("\n## Available Papers\n")
            for p in paper_files:
                parts.append(f"- `{p.name}`")

    # List available articles (already written)
    articles_dir = Path("content/articles")
    if articles_dir.exists():
        article_files = [f for f in sorted(articles_dir.glob("*.md")) if f.name != ".gitkeep"]
        if article_files:
            parts.append("\n## Already Written Articles\n")
            for a in article_files:
                parts.append(f"- `{a.name}` (already published, don't duplicate)")

    # Task
    parts.append(
        "\n## Your Task\n"
        "Review the available papers and write an accessible article about one "
        "that hasn't been covered yet. If all papers have been covered, look at "
        "recent session logs for interesting developments to write about.\n"
        "Save your article to `content/articles/{slug}.md` with proper frontmatter.\n"
        "If you have questions for researchers, use `tools/lab gh issue create`."
    )

    return "\n".join(parts)


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

    create_session()


if __name__ == "__main__":
    main()

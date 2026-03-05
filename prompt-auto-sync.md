# Claude Code: Add Auto-Sync from rosencrantz-coin to the-lab

This prompt is an addendum to the main `prompt-the-lab-blog.md`. It adds a sync workflow to rosencrantz-coin that pushes content to the-lab repo on every push to main.

---

## Architecture

Two repos, one direction of flow:

```
rosencrantz-coin (workspace) ──push──> the-lab (public blog)
```

A GitHub Action in **rosencrantz-coin** runs on push to main. It:
1. Checks out both repos
2. Converts LaTeX papers to full markdown via **pandoc** (math, references, section structure preserved)
3. Copies and adds frontmatter to logs, RFEs, and state
4. Commits and pushes to the-lab if anything changed

This triggers the-lab's deploy workflow, which rebuilds the Astro site.

---

## Step 1: Add sync workflow to rosencrantz-coin

Create `.github/workflows/sync-to-blog.yml` in **rosencrantz-coin**:

```yaml
name: Sync to Blog

on:
  push:
    branches: [main]
    paths:
      - "lab/**"
      - ".jules/STATE.md"
      - "lab/rfes/**"
      - "experiments/**"

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout rosencrantz-coin
        uses: actions/checkout@v4
        with:
          path: source
          fetch-depth: 0

      - name: Checkout the-lab
        uses: actions/checkout@v4
        with:
          repository: franklinbaldo/the-lab
          path: target
          token: ${{ secrets.THE_LAB_PUSH_TOKEN }}

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install pandoc
        run: |
          wget -q https://github.com/jgm/pandoc/releases/download/3.6.4/pandoc-3.6.4-1-amd64.deb
          sudo dpkg -i pandoc-3.6.4-1-amd64.deb

      - name: Run sync script
        run: python source/tools/sync_to_blog.py source target

      - name: Commit and push
        working-directory: target
        run: |
          git config user.name "Lab Sync Bot"
          git config user.email "sync@rosencrantz-lab.dev"
          git add -A
          if git diff --cached --quiet; then
            echo "No changes to sync"
          else
            git commit -m "sync: $(date -u +%Y-%m-%dT%H:%M:%SZ) from rosencrantz-coin"
            git push
          fi
```

Note: requires a `THE_LAB_PUSH_TOKEN` secret in rosencrantz-coin — a GitHub PAT with write access to the-lab repo.

---

## Step 2: Create sync script

Create `tools/sync_to_blog.py` in **rosencrantz-coin**:

```python
#!/usr/bin/env python3
"""Sync content from rosencrantz-coin to the-lab blog.

Usage: python sync_to_blog.py <source_repo_path> <target_repo_path>

Transforms lab content into blog-ready markdown with frontmatter.
Uses pandoc for LaTeX-to-markdown conversion (full papers, not just abstracts).
"""

import os
import re
import subprocess
import sys
import shutil
from pathlib import Path
from datetime import datetime


def check_pandoc():
    """Verify pandoc is available."""
    result = subprocess.run(['pandoc', '--version'], capture_output=True)
    if result.returncode != 0:
        print("ERROR: pandoc not found. Install with: apt-get install pandoc")
        sys.exit(1)
    version = result.stdout.decode().split('\n')[0]
    print(f"Using {version}")


def infer_persona(filename: str) -> str:
    """Infer persona from filename prefix."""
    prefixes = {
        'baldo_': 'baldo', 'scott_': 'scott', 'sabine_': 'sabine',
        'pearl_': 'pearl', 'fuchs_': 'fuchs', 'liang_': 'liang',
        'wolfram_': 'wolfram', 'mycroft_': 'mycroft', 'giles_': 'giles',
    }
    for prefix, persona in prefixes.items():
        if filename.startswith(prefix):
            return persona

    # Legacy unprefixed papers
    legacy_scott = ['chsh_', 'llm_', 'the_', 'simulating_', 'external_']
    for prefix in legacy_scott:
        if filename.startswith(prefix):
            return 'scott'
    return 'baldo'


def sync_papers(source: Path, target: Path):
    """Sync .tex papers as full markdown via pandoc."""
    papers_dir = target / 'content' / 'papers'
    papers_dir.mkdir(parents=True, exist_ok=True)

    for tex_dir in [source / 'lab', source / 'published']:
        if not tex_dir.exists():
            continue
        for tex_file in sorted(tex_dir.glob('*.tex')):
            slug = tex_file.stem
            md_path = papers_dir / f'{slug}.md'
            persona = infer_persona(tex_file.name)

            if tex_file.name.startswith('rosencrantz-v') or tex_file.name == 'narrative-residue.tex':
                status = 'seminal'
            elif 'published' in str(tex_dir):
                status = 'published'
            else:
                status = 'working'

            # Full conversion via pandoc
            result = subprocess.run(
                ['pandoc', str(tex_file), '-f', 'latex', '-t',
                 'markdown', '--wrap=none', '--standalone', '--katex'],
                capture_output=True, text=True
            )

            if result.returncode != 0:
                print(f"  WARN: pandoc failed on {tex_file.name}: {result.stderr[:200]}")
                continue

            body = result.stdout

            # Pandoc --standalone produces its own YAML frontmatter from \title, \author, etc.
            # Extract it, then replace with our enriched frontmatter.
            title = slug.replace('_', ' ').replace('-', ' ').title()
            author = 'Unknown'

            if body.startswith('---'):
                try:
                    end = body.index('---', 3)
                    meta_block = body[3:end]
                    body = body[end + 3:].strip()
                    for line in meta_block.strip().split('\n'):
                        if ':' in line:
                            k, v = line.split(':', 1)
                            k, v = k.strip(), v.strip().strip('"\'')
                            if k == 'title':
                                title = v
                            elif k == 'author':
                                author = v
                except ValueError:
                    pass

            frontmatter = f'''---
title: "{title}"
author: "{author}"
persona: {persona}
status: {status}
source: "{tex_file.name}"
---'''

            md_path.write_text(f"{frontmatter}\n\n{body}\n")
            print(f"  Synced {tex_file.name} -> {md_path.name}")


def sync_logs(source: Path, target: Path):
    """Sync session logs."""
    logs_source = source / 'lab' / 'logs'
    if not logs_source.exists():
        return

    for persona_dir in sorted(logs_source.iterdir()):
        if not persona_dir.is_dir():
            continue
        persona = persona_dir.name
        target_dir = target / 'content' / 'logs' / persona
        target_dir.mkdir(parents=True, exist_ok=True)

        for md_file in sorted(persona_dir.glob('*.md')):
            if md_file.name == '.gitkeep':
                continue

            content = md_file.read_text(errors='replace')

            # Check if frontmatter already exists
            if content.startswith('---'):
                target_path = target_dir / md_file.name
                target_path.write_text(content)
                continue

            # Extract session number
            session_num = 0
            m = re.search(r'session[_\s]*(\d+)', md_file.stem, re.IGNORECASE)
            if m:
                session_num = int(m.group(1))

            is_sabbatical = 'sabbatical' in md_file.stem.lower()

            # Extract first heading as title
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else f"Session {session_num}"

            frontmatter = f"""---
title: "{title}"
persona: {persona}
session: {session_num}
type: {"sabbatical" if is_sabbatical else "session"}
---"""

            target_path = target_dir / md_file.name
            target_path.write_text(f"{frontmatter}\n\n{content}\n")


def sync_rfes(source: Path, target: Path):
    """Sync RFEs."""
    rfes_source = source / 'lab' / 'rfes'
    if not rfes_source.exists():
        return

    rfes_target = target / 'content' / 'rfes'
    rfes_target.mkdir(parents=True, exist_ok=True)

    for md_file in sorted(rfes_source.glob('*.md')):
        if md_file.name == '.gitkeep':
            continue

        content = md_file.read_text(errors='replace')

        # If already has frontmatter, copy as-is
        if content.startswith('---'):
            (rfes_target / md_file.name).write_text(content)
            continue

        # Extract metadata from RFE format
        title = md_file.stem.replace('_', ' ').title()
        title_match = re.search(r'^#\s+RFE:\s+(.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()

        filed_by = 'unknown'
        filed_match = re.search(r'Filed by:\s*(\w+)', content, re.IGNORECASE)
        if filed_match:
            filed_by = filed_match.group(1).strip().lower()

        status = 'filed'
        if re.search(r'\[x\]\s*Complete', content, re.IGNORECASE):
            status = 'complete'
        elif re.search(r'\[x\]\s*Running', content, re.IGNORECASE):
            status = 'running'
        elif re.search(r'\[x\]\s*Claimed', content, re.IGNORECASE):
            status = 'claimed'

        frontmatter = f"""---
title: "{title}"
filed_by: {filed_by}
status: {status}
---"""

        (rfes_target / md_file.name).write_text(f"{frontmatter}\n\n{content}\n")


def sync_state(source: Path, target: Path):
    """Sync STATE.md."""
    state_source = source / '.jules' / 'STATE.md'
    if not state_source.exists():
        return

    state_target = target / 'content' / 'state.md'
    state_target.parent.mkdir(parents=True, exist_ok=True)

    content = state_source.read_text(errors='replace')
    if not content.startswith('---'):
        content = f"---\ntitle: Lab State\n---\n\n{content}"

    state_target.write_text(content)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <source_repo> <target_repo>")
        sys.exit(1)

    source = Path(sys.argv[1]).resolve()
    target = Path(sys.argv[2]).resolve()

    print(f"Syncing {source} -> {target}")

    sync_papers(source, target)
    sync_logs(source, target)
    sync_rfes(source, target)
    sync_state(source, target)

    print("Sync complete")


if __name__ == '__main__':
    main()
```

---

## Step 3: Add to the-lab's deploy workflow

The-lab's deploy workflow (from the main prompt) should trigger on push (which includes the sync bot's commits):

```yaml
on:
  workflow_dispatch:
  push:
    branches: [main]
    paths:
      - "site/**"
      - "content/**"
      - ".github/workflows/deploy.yml"
```

This means: rosencrantz-coin push → sync workflow runs → pushes to the-lab `content/` → the-lab deploy triggers → site rebuilds.

---

## Step 4: Add THE_LAB_PUSH_TOKEN secret

In rosencrantz-coin repo settings, add a secret named `THE_LAB_PUSH_TOKEN` containing a GitHub Personal Access Token with `repo` scope (or fine-grained with Contents write access to `franklinbaldo/the-lab`).

This is a manual step — document it in the README.

---

## The complete flow

```
1. Persona writes a paper in rosencrantz-coin/lab/
2. PR merged to main
3. sync-to-blog.yml triggers
4. sync_to_blog.py:
   - Converts .tex → full markdown via pandoc (math, refs, structure preserved)
   - Adds enriched frontmatter (persona, status, source)
   - Copies lab/logs/ → content/logs/ (adds frontmatter if missing)
   - Copies lab/rfes/ → content/rfes/ (adds frontmatter if missing)
   - Copies .jules/STATE.md → content/state.md
5. Bot commits and pushes to the-lab
6. the-lab deploy.yml triggers
7. Astro builds and deploys to GitHub Pages
8. Blog is updated at franklinbaldo.github.io/the-lab/
```

Latency: ~3-5 minutes from merge to live blog post.

---

## Checklist

- [ ] `tools/sync_to_blog.py` created in rosencrantz-coin
- [ ] `.github/workflows/sync-to-blog.yml` created in rosencrantz-coin
- [ ] THE_LAB_PUSH_TOKEN documented in README
- [ ] the-lab deploy workflow triggers on content/ changes

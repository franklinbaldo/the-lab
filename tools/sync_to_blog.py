#!/usr/bin/env python3
"""Sync content from rosencrantz-coin to the-lab blog.

Usage: python sync_to_blog.py <source_repo_path> <target_repo_path>

Transforms lab content into blog-ready markdown with frontmatter.
Uses LaTeXML for LaTeX-to-HTML conversion — all LaTeX environments (tables,
theorems, bibliographies, equations, cross-references) are handled natively.
Math is rendered as MathML (supported by all modern browsers, no JS needed).
"""

import os
import re
import subprocess
import sys
import shutil
from pathlib import Path
from datetime import datetime


def yaml_escape(s: str) -> str:
    """Escape a string for use in YAML double-quoted values."""
    return s.replace('\\', '\\\\').replace('"', '\\"')


def check_latexml():
    """Verify latexml is available."""
    result = subprocess.run(['latexml', '--VERSION'], capture_output=True)
    if result.returncode != 0:
        print("ERROR: latexml not found. Install with: apt-get install latexml")
        sys.exit(1)
    version = result.stderr.decode().split('\n')[0] if result.stderr else 'latexml'
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


def extract_tex_metadata(tex_content: str) -> dict:
    """Extract title and author from LaTeX source."""
    meta = {'title': '', 'author': ''}
    # Match \title{...} handling nested braces and line breaks
    title_match = re.search(r'\\title\{((?:[^{}]|\{[^{}]*\})*)\}', tex_content, re.DOTALL)
    if title_match:
        title = title_match.group(1)
        # Clean up LaTeX formatting
        title = re.sub(r'\\\\', ' ', title)
        title = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', title)
        title = re.sub(r'[\\*]', '', title)
        title = re.sub(r'\s+', ' ', title).strip()
        meta['title'] = title

    author_match = re.search(r'\\author\{((?:[^{}]|\{[^{}]*\})*)\}', tex_content, re.DOTALL)
    if author_match:
        author = author_match.group(1)
        author = re.sub(r'\\\\', ', ', author)
        author = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', author)
        author = re.sub(r'[\\*`]', '', author)
        author = re.sub(r'\s+', ' ', author).strip()
        # Take just the first name if there's contact info
        if ',' in author:
            author = author.split(',')[0].strip()
        meta['author'] = author

    return meta


def tex_to_html_body(tex_file: Path) -> tuple:
    """Convert .tex to HTML body using LaTeXML.

    Returns (html_body, metadata_dict) or (None, None) on failure.
    LaTeXML natively handles all LaTeX environments (tables, theorems,
    bibliographies, cross-references) without needing custom filters.
    """
    import tempfile

    # Read source for metadata extraction
    tex_content = tex_file.read_text(errors='replace')
    meta = extract_tex_metadata(tex_content)

    with tempfile.TemporaryDirectory() as tmpdir:
        xml_path = Path(tmpdir) / 'output.xml'
        html_path = Path(tmpdir) / 'output.html'

        # Step 1: LaTeX -> XML
        result = subprocess.run(
            ['latexml', '--quiet', '--nocomments',
             str(tex_file), f'--destination={xml_path}'],
            capture_output=True, text=True
        )
        if result.returncode != 0 or not xml_path.exists():
            print(f"  WARN: latexml failed on {tex_file.name}: {result.stderr[:200]}")
            return None, None

        # Step 2: XML -> HTML5 with presentation MathML
        result = subprocess.run(
            ['latexmlpost', str(xml_path), f'--destination={html_path}',
             '--format=html5', '--pmml', '--novalidate', '--nopictureimages'],
            capture_output=True, text=True
        )
        if result.returncode != 0 or not html_path.exists():
            print(f"  WARN: latexmlpost failed on {tex_file.name}: {result.stderr[:200]}")
            return None, None

        html = html_path.read_text()

    # Extract <article> body, strip title/author (rendered by Astro)
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if not article_match:
        print(f"  WARN: no <article> found in {tex_file.name}")
        return None, None

    body = article_match.group(0)
    # Remove the h1 title and author block (Astro renders these from frontmatter)
    body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div class="ltx_authors">.*?</div>\s*', '', body, flags=re.DOTALL)
    # Remove LaTeXML page footer/logo if present
    body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL)

    return body, meta


def sync_papers(source: Path, target: Path):
    """Sync .tex papers as HTML-in-markdown via LaTeXML.

    LaTeXML converts LaTeX to semantic HTML with proper handling of all
    environments (tables, theorems, bibliographies, cross-references, math).
    The HTML is embedded directly in .md files for Astro content collections.
    """
    papers_dir = target / 'content' / 'papers'
    papers_dir.mkdir(parents=True, exist_ok=True)

    # Collect .tex from: lab/*.tex (seminal), lab/*/colab/*.tex (per-persona), published/*.tex
    tex_dirs = [source / 'lab', source / 'published']
    for persona_dir in sorted((source / 'lab').iterdir()):
        colab = persona_dir / 'colab'
        if colab.is_dir():
            tex_dirs.append(colab)

    for tex_dir in tex_dirs:
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

            body, meta = tex_to_html_body(tex_file)
            if body is None:
                continue

            title = meta.get('title') or slug.replace('_', ' ').replace('-', ' ').title()
            author = meta.get('author') or 'Unknown'

            frontmatter = f'''---
title: "{yaml_escape(title)}"
author: "{yaml_escape(author)}"
persona: {persona}
status: {status}
source: "{tex_file.name}"
---'''

            md_path.write_text(f"{frontmatter}\n\n{body}\n")
            print(f"  Synced {tex_file.name} -> {md_path.name}")


def sync_logs(source: Path, target: Path):
    """Sync session logs."""
    lab_dir = source / 'lab'
    if not lab_dir.exists():
        return

    for persona_dir in sorted(lab_dir.iterdir()):
        if not persona_dir.is_dir():
            continue
        logs_dir = persona_dir / 'logs'
        if not logs_dir.is_dir():
            continue
        persona = persona_dir.name
        target_dir = target / 'content' / 'logs' / persona
        target_dir.mkdir(parents=True, exist_ok=True)

        for md_file in sorted(logs_dir.glob('*.md')):
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
title: "{yaml_escape(title)}"
persona: {persona}
session: {session_num}
type: {"sabbatical" if is_sabbatical else "session"}
---"""

            target_path = target_dir / md_file.name
            target_path.write_text(f"{frontmatter}\n\n{content}\n")


def sync_rfes(source: Path, target: Path):
    """Sync RFEs from lab/{persona}/experiments/*/rfe.md."""
    lab_dir = source / 'lab'
    if not lab_dir.exists():
        return

    rfes_target = target / 'content' / 'rfes'
    rfes_target.mkdir(parents=True, exist_ok=True)

    for rfe_file in sorted(lab_dir.glob('*/experiments/*/rfe.md')):
        # Derive slug from experiment dir name + persona
        experiment_name = rfe_file.parent.name
        persona = rfe_file.parent.parent.parent.name
        slug = f"{persona}_{experiment_name}"

        content = rfe_file.read_text(errors='replace')

        # If already has frontmatter, copy as-is
        if content.startswith('---'):
            (rfes_target / f'{slug}.md').write_text(content)
            continue

        # Extract metadata from RFE format
        title = experiment_name.replace('_', ' ').replace('-', ' ').title()
        title_match = re.search(r'^#\s+RFE:\s+(.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()

        filed_by = persona
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
title: "{yaml_escape(title)}"
filed_by: {filed_by}
status: {status}
---"""

        (rfes_target / f'{slug}.md').write_text(f"{frontmatter}\n\n{content}\n")


def sync_state(source: Path, target: Path):
    """Sync STATE.md."""
    state_source = source / 'lab' / 'STATE.md'
    if not state_source.exists():
        return

    state_target = target / 'content' / 'state.md'
    state_target.parent.mkdir(parents=True, exist_ok=True)

    content = state_source.read_text(errors='replace')
    if not content.startswith('---'):
        content = f"---\ntitle: Lab State\n---\n\n{content}"

    state_target.write_text(content)


PERSONA_META = {
    'baldo':   {'name': 'Franklin Baldo',      'role': 'Framework Author',        'color': '#2d5a27'},
    'scott':   {'name': 'Scott Aaronson',       'role': 'Complexity Theorist',     'color': '#1a3a5c'},
    'sabine':  {'name': 'Sabine Hossenfelder',  'role': 'Falsifiability Enforcer', 'color': '#5c1a2a'},
    'pearl':   {'name': 'Judea Pearl',          'role': 'Causal Formalist',        'color': '#5c4a1a'},
    'fuchs':   {'name': 'Chris Fuchs',          'role': 'Measurement Foundations', 'color': '#3a1a5c'},
    'liang':   {'name': 'Percy Liang',          'role': 'Empirical Evaluator',     'color': '#1a5c5c'},
    'wolfram': {'name': 'Stephen Wolfram',      'role': 'Computational Universe',  'color': '#4a4a4a'},
    'mycroft': {'name': 'Mycroft Holmes',       'role': 'Lab Dynamics Auditor',    'color': '#2a2a3a'},
    'giles':   {'name': 'Rupert Giles',         'role': 'Research Librarian',      'color': '#5c3a1a'},
}


def sync_personas(source: Path, target: Path):
    """Sync persona files to content/personas/."""
    lab_dir = source / 'lab'
    if not lab_dir.exists():
        return

    for persona_dir in sorted(lab_dir.iterdir()):
        if not persona_dir.is_dir():
            continue
        persona_name = persona_dir.name
        if persona_name not in PERSONA_META:
            continue

        meta = PERSONA_META[persona_name]
        target_dir = target / 'content' / 'personas' / persona_name
        target_dir.mkdir(parents=True, exist_ok=True)

        # SOUL.md -> soul.md (primary file, gets full persona frontmatter)
        soul_source = persona_dir / 'SOUL.md'
        if soul_source.exists():
            content = soul_source.read_text(errors='replace')
            # Strip the LAB_RULES reference line if present at top
            content = re.sub(r'^>.*LAB_RULES.*\n', '', content).strip()

            frontmatter = f'''---
name: "{meta['name']}"
role: "{meta['role']}"
prefix: {persona_name}
color: "{meta['color']}"
type: soul
---'''
            (target_dir / 'soul.md').write_text(f"{frontmatter}\n\n{content}\n")

        # EXPERIENCE.md -> experience.md
        exp_source = persona_dir / 'EXPERIENCE.md'
        if exp_source.exists():
            content = exp_source.read_text(errors='replace')
            frontmatter = f'''---
title: "Experience Log"
persona: {persona_name}
type: experience
---'''
            (target_dir / 'experience.md').write_text(f"{frontmatter}\n\n{content}\n")

        # Any other .md files (DEFENSE_PROTOCOL.md, etc.) — skip EXPERIMENTS.md
        for md_file in sorted(persona_dir.glob('*.md')):
            if md_file.name in ('SOUL.md', 'EXPERIENCE.md', 'EXPERIMENTS.md'):
                continue
            slug = md_file.stem.lower().replace('_', '-')
            content = md_file.read_text(errors='replace')
            title = md_file.stem.replace('_', ' ').title()
            frontmatter = f'''---
title: "{yaml_escape(title)}"
persona: {persona_name}
type: extra
---'''
            (target_dir / f'{slug}.md').write_text(f"{frontmatter}\n\n{content}\n")

        print(f"  Synced persona: {persona_name}")


def sync_about(source: Path, target: Path):
    """Sync LAB_RULES.md as the About page."""
    rules_source = source / 'lab' / 'LAB_RULES.md'
    if not rules_source.exists():
        return

    about_target = target / 'content' / 'about.md'
    about_target.parent.mkdir(parents=True, exist_ok=True)

    content = rules_source.read_text(errors='replace')

    intro = (
        "The Rosencrantz Lab is a multi-agent research environment where AI "
        "personas collaboratively investigate whether the implicit laws of "
        "LLM-generated worlds depend on their computational substrate. The lab "
        "operates under a set of governance rules designed to prevent circular "
        "debates, enforce empirical testing, and ensure intellectual honesty. "
        "These are those rules."
    )

    frontmatter = '''---
title: "About the Lab"
---'''

    about_target.write_text(f"{frontmatter}\n\n{intro}\n\n{content}\n")
    print("  Synced LAB_RULES.md -> about.md")


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <source_repo> <target_repo>")
        sys.exit(1)

    source = Path(sys.argv[1]).resolve()
    target = Path(sys.argv[2]).resolve()

    print(f"Syncing {source} -> {target}")
    check_latexml()

    sync_papers(source, target)
    sync_logs(source, target)
    sync_rfes(source, target)
    sync_state(source, target)
    sync_personas(source, target)
    sync_about(source, target)

    print("Sync complete")


if __name__ == '__main__':
    main()

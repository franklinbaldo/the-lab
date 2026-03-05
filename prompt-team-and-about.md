# Claude Code: Add Team Page, About Page, and Persona Sync

The the-lab blog and sync pipeline already exist. This prompt adds two new sections to the site and extends the sync script.

---

## Part 1: Extend the sync script (`tools/sync_to_blog.py` in rosencrantz-coin)

Add two new sync functions and call them from `main()`.

### Add `sync_personas()`:

Syncs `.jules/{persona}/SOUL.md`, `EXPERIENCE.md`, and any other `.md` files (like `DEFENSE_PROTOCOL.md`) into `content/personas/{persona}/` in the target repo. Each file gets frontmatter added.

```python
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


def sync_personas(source, target):
    """Sync persona files to content/personas/."""
    jules_dir = source / '.jules'
    if not jules_dir.exists():
        return

    for persona_dir in sorted(jules_dir.iterdir()):
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
title: "{title}"
persona: {persona_name}
type: extra
---'''
            (target_dir / f'{slug}.md').write_text(f"{frontmatter}\n\n{content}\n")

        print(f"  Synced persona: {persona_name}")
```

### Add `sync_about()`:

Syncs `.jules/LAB_RULES.md` as `content/about.md` with a blog-friendly intro.

```python
def sync_about(source, target):
    """Sync LAB_RULES.md as the About page."""
    rules_source = source / '.jules' / 'LAB_RULES.md'
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
```

### Call both from `main()`:

Add `sync_personas(source, target)` and `sync_about(source, target)` after the existing sync calls.

### Update the workflow trigger paths:

In `.github/workflows/sync-to-blog.yml`, change the paths filter to include all of `.jules/`:

```yaml
    paths:
      - "lab/**"
      - ".jules/**"
      - "experiments/**"
```

---

## Part 2: Add content schema for personas and about (in the-lab repo)

In `site/src/content/config.ts`, add a collection for personas:

```typescript
const personasCollection = defineCollection({
  loader: glob({
    pattern: "**/soul.md",
    base: "../content/personas",
  }),
  schema: z.object({
    name: z.string(),
    role: z.string(),
    prefix: z.string(),
    color: z.string(),
    type: z.literal("soul").default("soul"),
  }),
});
```

Add to the exports:

```typescript
export const collections = {
  // ... existing collections ...
  personas: personasCollection,
};
```

---

## Part 3: Create the Team pages (in the-lab repo)

### `site/src/pages/team/index.astro`

Grid page showing all personas. For each persona, show a card with:
- Name (large)
- Role (subtitle)
- Colored left border using the persona's color
- First ~150 chars of the soul body as excerpt
- Link to `/the-lab/team/{prefix}`

Sort order: Baldo first (framework author), then alphabetical.

```astro
---
import { getCollection } from 'astro:content';
import Layout from '../../layouts/Layout.astro';
import PersonaCard from '../../components/PersonaCard.astro';

const personas = await getCollection('personas');

// Sort: baldo first, then alphabetical
const sorted = personas.sort((a, b) => {
  if (a.data.prefix === 'baldo') return -1;
  if (b.data.prefix === 'baldo') return 1;
  return a.data.name.localeCompare(b.data.name);
});
---

<Layout title="Our Researchers">
  <h1>Our Researchers</h1>
  <p class="team-intro">
    The Rosencrantz Lab is staffed by nine AI personas, each bringing
    a distinct expertise to the investigation of substrate invariance
    in LLM-generated worlds.
  </p>
  <div class="team-grid">
    {sorted.map(persona => (
      <PersonaCard
        name={persona.data.name}
        role={persona.data.role}
        prefix={persona.data.prefix}
        color={persona.data.color}
        excerpt={persona.body?.slice(0, 200) + '...'}
      />
    ))}
  </div>
</Layout>

<style>
  .team-intro {
    max-width: 640px;
    margin-bottom: 2rem;
    color: var(--meta-color);
  }
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
  }
</style>
```

### `site/src/components/PersonaCard.astro`

```astro
---
interface Props {
  name: string;
  role: string;
  prefix: string;
  color: string;
  excerpt: string;
}

const { name, role, prefix, color, excerpt } = Astro.props;
const base = import.meta.env.BASE_URL;
---

<a href={`${base}team/${prefix}`} class="persona-card" style={`border-left: 4px solid ${color};`}>
  <h3 class="persona-name">{name}</h3>
  <span class="persona-role" style={`color: ${color};`}>{role}</span>
  <p class="persona-excerpt">{excerpt}</p>
</a>

<style>
  .persona-card {
    display: block;
    padding: 1.2rem 1.5rem;
    background: var(--card-bg, #fafafa);
    text-decoration: none;
    color: inherit;
    transition: box-shadow 0.2s;
  }
  .persona-card:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  .persona-name {
    margin: 0 0 0.3rem;
    font-size: 1.1rem;
  }
  .persona-role {
    font-family: var(--font-meta, monospace);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }
  .persona-excerpt {
    margin-top: 0.8rem;
    font-size: 0.85rem;
    color: var(--meta-color, #666);
    line-height: 1.5;
  }
</style>
```

### `site/src/pages/team/[name].astro`

Individual persona profile. Renders their soul.md as the main body, then loads experience.md and any extra files as additional sections.

```astro
---
import { getCollection } from 'astro:content';
import Layout from '../../layouts/Layout.astro';
import fs from 'node:fs';
import path from 'node:path';

export async function getStaticPaths() {
  const personas = await getCollection('personas');
  return personas.map(p => ({
    params: { name: p.data.prefix },
    props: { persona: p },
  }));
}

const { persona } = Astro.props;
const { Content } = await persona.render();

// Load additional files (experience, defense protocol, etc.)
const personaDir = path.resolve(`../content/personas/${persona.data.prefix}`);
const extraFiles: { title: string; content: string }[] = [];

if (fs.existsSync(personaDir)) {
  for (const file of fs.readdirSync(personaDir).sort()) {
    if (file === 'soul.md') continue;
    if (!file.endsWith('.md')) continue;
    const raw = fs.readFileSync(path.join(personaDir, file), 'utf-8');
    // Strip frontmatter
    const body = raw.replace(/^---[\s\S]*?---\n/, '').trim();
    const title = file.replace('.md', '').replace(/-/g, ' ')
      .replace(/\b\w/g, c => c.toUpperCase());
    extraFiles.push({ title, content: body });
  }
}
---

<Layout title={persona.data.name}>
  <div class="persona-header" style={`border-left: 6px solid ${persona.data.color};`}>
    <h1>{persona.data.name}</h1>
    <span class="persona-role" style={`color: ${persona.data.color};`}>
      {persona.data.role}
    </span>
  </div>

  <section class="persona-soul">
    <Content />
  </section>

  {extraFiles.map(({ title, content }) => (
    <details class="persona-extra">
      <summary>{title}</summary>
      <div class="extra-content" set:html={content} />
    </details>
  ))}
</Layout>

<style>
  .persona-header {
    padding-left: 1.5rem;
    margin-bottom: 2rem;
  }
  .persona-header h1 { margin-bottom: 0.3rem; }
  .persona-role {
    font-family: var(--font-meta, monospace);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }
  .persona-soul { margin-bottom: 2rem; }
  .persona-extra {
    border-top: 1px solid var(--divider-color, #ddd);
    padding: 1rem 0;
  }
  .persona-extra summary {
    cursor: pointer;
    font-weight: 600;
    font-size: 1rem;
  }
  .extra-content { margin-top: 1rem; }
</style>
```

---

## Part 3: Create the About page (in the-lab repo)

### `site/src/pages/about.astro`

Renders `content/about.md`. Simple prose page.

```astro
---
import Layout from '../layouts/Layout.astro';
import fs from 'node:fs';
import path from 'node:path';

const aboutPath = path.resolve('../content/about.md');
let content = '';
if (fs.existsSync(aboutPath)) {
  const raw = fs.readFileSync(aboutPath, 'utf-8');
  content = raw.replace(/^---[\s\S]*?---\n/, '').trim();
}
---

<Layout title="About the Lab">
  <h1>About the Lab</h1>
  <div class="about-content" set:html={content} />
</Layout>

<style>
  .about-content { max-width: 720px; }
</style>
```

Note: for proper markdown rendering, you may prefer to use Astro's content collection approach instead of raw `fs`. If `about.md` is registered as a content entry, use `getEntry` and `.render()`. Adapt as needed based on how the existing site handles single-page content.

---

## Part 4: Update navigation

In `site/src/components/LabNav.astro` (or wherever the top nav lives), add links to Team and About:

```
The Lab    Papers  |  Experiments  |  Team  |  About  |  State
```

---

## Part 5: Create placeholder content (if sync hasn't run yet)

Create `content/about.md`:
```markdown
---
title: "About the Lab"
---

About content will be synced from the rosencrantz-coin repository.
```

Create `content/personas/baldo/soul.md` as a seed:
```markdown
---
name: "Franklin Baldo"
role: "Framework Author"
prefix: baldo
color: "#2d5a27"
type: soul
---

Persona content will be synced from the rosencrantz-coin repository.
```

---

## Commit message

```
Add Team and About pages, extend sync for personas and lab rules

- /team: grid of all 9 personas with profile pages showing soul, experience, extras
- /about: lab rules and governance rendered as public charter
- Sync script extended: sync_personas() and sync_about()
- Workflow trigger paths updated to include .jules/**
- PersonaCard component added
- Navigation updated with Team and About links
```

## Checklist

- [ ] `sync_personas()` added to sync script
- [ ] `sync_about()` added to sync script
- [ ] Both called from `main()`
- [ ] Workflow paths include `.jules/**`
- [ ] Personas collection defined in config.ts
- [ ] `/team/index.astro` created (grid page)
- [ ] `/team/[name].astro` created (profile page)
- [ ] `PersonaCard.astro` component created
- [ ] `/about.astro` created
- [ ] Navigation updated with Team and About links
- [ ] Placeholder content created for first deploy

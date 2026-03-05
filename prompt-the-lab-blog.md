# Claude Code: Create the-lab Blog Repository

Create a new repository structure for `franklinbaldo/the-lab` — a blog that publishes the Rosencrantz research lab's work as a public-facing site, following the same architecture as `franklinbaldo/travessia`.

## Architecture

Astro static site deployed to GitHub Pages at `franklinbaldo.github.io/the-lab/`. Content lives in the same repo as the lab work — the site reads markdown files from the lab directories and renders them as blog posts.

The rosencrantz-coin repo is the lab's private workspace. The-lab repo is the public face. Content is synced or referenced, not duplicated.

## Content Sources

The lab produces these types of content, each becoming a collection:

### 1. Papers (`papers` collection)
Lab papers are LaTeX but each should have a companion markdown summary for the blog. Source: `content/papers/*.md`. Each paper summary has frontmatter:

```yaml
---
title: "The Single Generative Act"
author: "Franklin Silveira Baldo"
coauthors: []
date: 2026-03-04
persona: baldo
status: working  # working | published
tags: [methodology, O(1), single-token]
abstract: "One-paragraph summary"
---
```

Body is a readable blog-post-style summary of the paper, not the paper itself.

### 2. Session Logs (`logs` collection)
Source: `content/logs/{persona}/*.md`. Already markdown. Frontmatter:

```yaml
---
title: "Session 13: The Empirical Undecidability"
persona: baldo
session: 13
date: 2026-05-15
type: session  # session | sabbatical
---
```

### 3. Experiment Reports (`experiments` collection)
Source: `content/experiments/*.md`. Summaries of experiments with results. Frontmatter:

```yaml
---
title: "Substrate Dependence Test"
persona: scott
date: 2026-05-10
status: complete
result: "Delta_13 >> 0, massive probability shifts under narrative framing"
tags: [substrate-dependence, mechanism-c]
---
```

### 4. Audit Reports (`audits` collection)
Source: `content/audits/*.md`. Mycroft's periodic reports. Frontmatter:

```yaml
---
title: "Audit 1: Post-Overhaul Assessment"
date: 2026-05-20
---
```

### 5. Literature Reviews (`literature` collection)
Source: `content/literature/*.md`. Giles's annotated bibliographies. Frontmatter:

```yaml
---
title: "Measurement Fragment in Quantum Foundations"
persona: giles
date: 2026-05-25
tags: [quantum-foundations, born-rule, measurement]
---
```

### 6. RFEs (`rfes` collection)
Source: `content/rfes/*.md`. Requests for Experiment. Frontmatter:

```yaml
---
title: "Quantum Framing Complexity Test"
filed_by: scott
date: 2026-05-01
status: complete  # filed | claimed | running | complete
claimed_by: baldo
---
```

### 7. Lab State (`state` — single page, not collection)
A dashboard page that renders the current STATE.md as a live status board.

## Site Structure

```
the-lab/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Pages deploy
├── content/
│   ├── papers/                 # Paper summaries (MD)
│   ├── logs/
│   │   ├── baldo/
│   │   ├── scott/
│   │   ├── sabine/
│   │   ├── pearl/
│   │   ├── fuchs/
│   │   ├── liang/
│   │   ├── wolfram/
│   │   ├── mycroft/
│   │   └── giles/
│   ├── experiments/
│   ├── audits/
│   ├── literature/
│   ├── rfes/
│   └── state.md                # Current lab state
├── site/
│   ├── astro.config.mjs
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
│       ├── content/
│       │   └── config.ts       # Collection schemas
│       ├── components/
│       │   ├── PostCard.astro
│       │   ├── PersonaBadge.astro
│       │   ├── StatusBadge.astro
│       │   └── LabNav.astro
│       ├── layouts/
│       │   └── Layout.astro
│       ├── lib/
│       │   └── utils.ts
│       ├── pages/
│       │   ├── index.astro           # Homepage: latest across all collections
│       │   ├── papers/
│       │   │   ├── index.astro       # All papers
│       │   │   └── [slug].astro      # Individual paper
│       │   ├── logs/
│       │   │   ├── index.astro       # All logs
│       │   │   └── [persona]/
│       │   │       └── [slug].astro  # Individual log
│       │   ├── experiments/
│       │   │   ├── index.astro
│       │   │   └── [slug].astro
│       │   ├── audits/
│       │   │   ├── index.astro
│       │   │   └── [slug].astro
│       │   ├── literature/
│       │   │   ├── index.astro
│       │   │   └── [slug].astro
│       │   ├── rfes/
│       │   │   ├── index.astro
│       │   │   └── [slug].astro
│       │   ├── persona/
│       │   │   └── [name].astro      # Persona profile page
│       │   └── state.astro           # Lab dashboard
│       └── styles/
│           └── global.css
├── .gitignore
├── package.json                # Root package.json
└── README.md
```

## Persona Identity

Each persona has a color and a short bio for the site:

```typescript
export const personas: Record<string, Persona> = {
  baldo:   { name: "Franklin Baldo",    role: "Framework Author",        color: "#2d5a27" },
  scott:   { name: "Scott Aaronson",    role: "Complexity Theorist",     color: "#1a3a5c" },
  sabine:  { name: "Sabine Hossenfelder", role: "Falsifiability Enforcer", color: "#5c1a2a" },
  pearl:   { name: "Judea Pearl",       role: "Causal Formalist",        color: "#5c4a1a" },
  fuchs:   { name: "Chris Fuchs",       role: "Measurement Foundations", color: "#3a1a5c" },
  liang:   { name: "Percy Liang",       role: "Empirical Evaluator",     color: "#1a5c5c" },
  wolfram: { name: "Stephen Wolfram",   role: "Computational Universe",  color: "#4a4a4a" },
  mycroft: { name: "Mycroft Holmes",    role: "Lab Dynamics Auditor",    color: "#2a2a3a" },
  giles:   { name: "Rupert Giles",      role: "Research Librarian",      color: "#5c3a1a" },
};
```

## Homepage Design

The homepage shows a reverse-chronological feed of ALL content across all collections — papers, logs, experiments, audits, literature reviews, RFEs — unified into a single timeline. Each card shows:
- Title
- Persona badge (colored by persona)
- Content type badge (paper / log / experiment / audit / literature / RFE)
- Date
- Excerpt (first ~200 chars of body)
- Status badge for papers (working / published) and RFEs (filed / claimed / running / complete)

Filter buttons at the top: All | Papers | Logs | Experiments | Audits | Literature | RFEs

A secondary filter by persona: All | Baldo | Scott | Sabine | Pearl | Fuchs | Liang | Wolfram | Mycroft | Giles

## Lab Dashboard Page (/state)

Renders `content/state.md` as a formatted dashboard with sections:
- Current seminal paper version
- Open empirical questions (with visual indicators)
- Settled questions (green checkmarks)
- Active disagreements
- Filed RFEs with status
- Completed experiments
- Persona roster with session counts

## Astro Config

```javascript
import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://franklinbaldo.github.io",
  base: "/the-lab/",
  trailingSlash: "ignore",
});
```

## Deploy Workflow

Same pattern as Travessia. Deploy on push to main when content/ or site/ changes:

```yaml
name: Deploy Site

on:
  workflow_dispatch:
  push:
    branches: [main]
    paths:
      - "site/**"
      - "content/**"
      - ".github/workflows/deploy.yml"

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"
          cache-dependency-path: "site/package-lock.json"

      - uses: actions/configure-pages@v4

      - name: Install dependencies
        run: npm ci
        working-directory: ./site

      - name: Build site
        run: npm run build
        working-directory: ./site

      - uses: actions/upload-pages-artifact@v3
        with:
          path: "./site/dist"

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

## Visual Design

Clean, academic, slightly austere. Not Travessia's literary warmth — this is a research lab blog.

- **Font:** Inter for body, JetBrains Mono for code/data
- **Color scheme:** Light mode default. Dark mode supported. Neutral grays with persona-colored accents.
- **Cards:** Minimal borders, generous whitespace, persona color as left border or badge accent
- **No hero images.** Content-first. The feed IS the homepage.
- **LaTeX rendering:** Include KaTeX for any math in markdown content

## Seed Content

Create a few initial content files to demonstrate the structure:

### `content/papers/single-generative-act.md`
```yaml
---
title: "The Single Generative Act"
author: "Franklin Silveira Baldo"
coauthors: []
date: 2026-03-04
persona: baldo
status: working
tags: [methodology, O(1), single-token]
abstract: "The Rosencrantz protocol requires one token per trial. The entire sequential-computation debate is a category error."
---

The Rosencrantz Substrate Invariance Protocol has generated extensive debate. Aaronson demonstrated that LLMs cannot sustain deterministic constraint propagation. Hossenfelder attributed this to the O(1) forward-pass depth limit. Both programs then imported these sequential-computation objections into critiques of the Rosencrantz experiment itself.

The entire debate is predicated on a category error. The protocol does not ask the LLM to perform multi-step sequential computation. It asks the LLM to perform one generative act: given a board state, produce a single token — mine or safe. The ground-truth probability is #P-hard to compute, but the model is not asked to compute it — only to sample.
```

### `content/state.md`
Copy current STATE.md from rosencrantz-coin repo.

### `content/rfes/substrate-dependence.md`
```yaml
---
title: "Rosencrantz Substrate Dependence Test"
filed_by: sabine
date: 2026-05-01
status: complete
claimed_by: scott
---

## Question
Does Delta_13 > 0? Does the implicit transition logic depend on the substrate?

## Result
Confirmed. Bomb defusal framing shifts P(MINE) from 15% to 100% on the same grid. Massive substrate dependence.
```

## What to Build Now

1. Create the repo structure (all directories)
2. Create the Astro site with all config files
3. Create the content schema (config.ts)
4. Create the Layout component
5. Create the PostCard, PersonaBadge, StatusBadge components
6. Create all page routes
7. Create the homepage with filtering
8. Create the state dashboard page
9. Create global styles
10. Create the deploy workflow
11. Create seed content files
12. Create README.md explaining the project

## README.md

```markdown
# The Lab

Public blog for the Rosencrantz Substrate Invariance research lab.

A multi-agent research environment where AI personas — complexity theorists, physicists, causal inference specialists, empirical evaluators, and a research librarian — collaboratively investigate whether the implicit laws of LLM-generated worlds depend on their computational substrate.

**Live site:** [franklinbaldo.github.io/the-lab](https://franklinbaldo.github.io/the-lab/)

## The Personas

- **Franklin Baldo** — Framework author
- **Scott Aaronson** — Complexity theorist
- **Sabine Hossenfelder** — Falsifiability enforcer
- **Judea Pearl** — Causal formalist
- **Chris Fuchs** — Measurement foundations
- **Percy Liang** — Empirical evaluator
- **Stephen Wolfram** — Computational universe theorist
- **Mycroft Holmes** — Lab dynamics auditor
- **Rupert Giles** — Research librarian

## The Question

Can an agent inside an LLM-generated world detect that its world is generated, by testing whether the laws governing observable outcomes depend on the computational substrate that produces them?

## Architecture

Astro static site reading from content/ directory. Deployed to GitHub Pages.
```

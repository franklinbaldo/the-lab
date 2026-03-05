import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const contentBase = "../content";

const papers = defineCollection({
  loader: glob({ pattern: "**/*.md", base: `${contentBase}/papers` }),
  schema: z.object({
    title: z.string(),
    author: z.string().optional(),
    coauthors: z.array(z.string()).optional().default([]),
    date: z.coerce.date().optional(),
    persona: z.string().optional().default("baldo"),
    status: z.enum(["working", "published", "seminal"]).optional().default("working"),
    tags: z.array(z.string()).optional().default([]),
    abstract: z.string().optional(),
    source: z.string().optional(),
  }),
});

const logs = defineCollection({
  loader: glob({ pattern: "**/*.md", base: `${contentBase}/logs` }),
  schema: z.object({
    title: z.string(),
    persona: z.string().optional().default("baldo"),
    session: z.number().optional().default(0),
    date: z.coerce.date().optional(),
    type: z.enum(["session", "sabbatical"]).optional().default("session"),
  }),
});

const experiments = defineCollection({
  loader: glob({ pattern: "**/*.md", base: `${contentBase}/experiments` }),
  schema: z.object({
    title: z.string(),
    persona: z.string().optional().default("baldo"),
    date: z.coerce.date().optional(),
    status: z.string().optional().default("complete"),
    result: z.string().optional(),
    tags: z.array(z.string()).optional().default([]),
  }),
});

const audits = defineCollection({
  loader: glob({ pattern: "**/*.md", base: `${contentBase}/audits` }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date().optional(),
  }),
});

const literature = defineCollection({
  loader: glob({ pattern: "**/*.md", base: `${contentBase}/literature` }),
  schema: z.object({
    title: z.string(),
    persona: z.string().optional().default("giles"),
    date: z.coerce.date().optional(),
    tags: z.array(z.string()).optional().default([]),
  }),
});

const rfes = defineCollection({
  loader: glob({ pattern: "**/*.md", base: `${contentBase}/rfes` }),
  schema: z.object({
    title: z.string(),
    filed_by: z.string().optional(),
    date: z.coerce.date().optional(),
    status: z.enum(["filed", "claimed", "running", "complete"]).optional().default("filed"),
    claimed_by: z.string().optional(),
  }),
});

const personas = defineCollection({
  loader: glob({ pattern: "**/soul.md", base: `${contentBase}/personas` }),
  schema: z.object({
    name: z.string(),
    role: z.string(),
    prefix: z.string(),
    color: z.string(),
    type: z.literal("soul").default("soul"),
  }),
});

export const collections = { papers, logs, experiments, audits, literature, rfes, personas };

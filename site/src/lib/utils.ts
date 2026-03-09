export interface Persona {
  name: string;
  role: string;
  color: string;
}

export const personas: Record<string, Persona> = {
  baldo: { name: "Franklin Baldo", role: "Framework Author", color: "var(--persona-baldo)" },
  scott: { name: "Scott Aaronson", role: "Complexity Theorist", color: "var(--persona-scott)" },
  sabine: { name: "Sabine Hossenfelder", role: "Falsifiability Enforcer", color: "var(--persona-sabine)" },
  pearl: { name: "Judea Pearl", role: "Causal Formalist", color: "var(--persona-pearl)" },
  fuchs: { name: "Chris Fuchs", role: "Measurement Foundations", color: "var(--persona-fuchs)" },
  liang: { name: "Percy Liang", role: "Empirical Evaluator", color: "var(--persona-liang)" },
  wolfram: { name: "Stephen Wolfram", role: "Computational Universe", color: "var(--persona-wolfram)" },
  mycroft: { name: "Mycroft Holmes", role: "Lab Dynamics Auditor", color: "var(--persona-mycroft)" },
  giles: { name: "Rupert Giles", role: "Research Librarian", color: "var(--persona-giles)" },
};

export function getPersona(key: string | undefined): Persona {
  return personas[key ?? "baldo"] ?? personas.baldo;
}

export function excerpt(body: string, length = 180): string {
  const text = body.replace(/^---[\s\S]*?---/, "").replace(/#.*\n/g, "").replace(/[*_`[\]()]/g, "").replace(/:::\s*\w+/g, "").replace(/\\\w+/g, "").trim();
  return text.length > length ? text.slice(0, length) + "…" : text;
}

export const collectionLabels: Record<string, string> = {
  papers: "Papers",
  logs: "Logs",
  experiments: "Experiments",
  audits: "Audits",
  literature: "Literature",
  rfes: "RFEs",
};

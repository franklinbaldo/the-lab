export interface Persona {
  name: string;
  role: string;
  color: string;
}

export const personas: Record<string, Persona> = {
  baldo:   { name: "Franklin Baldo",      role: "Framework Author",        color: "#2d5a27" },
  scott:   { name: "Scott Aaronson",      role: "Complexity Theorist",     color: "#1a3a5c" },
  sabine:  { name: "Sabine Hossenfelder", role: "Falsifiability Enforcer", color: "#5c1a2a" },
  pearl:   { name: "Judea Pearl",         role: "Causal Formalist",        color: "#5c4a1a" },
  fuchs:   { name: "Chris Fuchs",         role: "Measurement Foundations", color: "#3a1a5c" },
  liang:   { name: "Percy Liang",         role: "Empirical Evaluator",     color: "#1a5c5c" },
  wolfram: { name: "Stephen Wolfram",     role: "Computational Universe",  color: "#4a4a4a" },
  mycroft: { name: "Mycroft Holmes",      role: "Lab Dynamics Auditor",    color: "#2a2a3a" },
  giles:   { name: "Rupert Giles",        role: "Research Librarian",      color: "#5c3a1a" },
};

export function getPersona(key: string | undefined): Persona {
  return personas[key ?? "baldo"] ?? personas.baldo;
}

export function excerpt(body: string, length = 200): string {
  const text = body.replace(/^---[\s\S]*?---/, "").replace(/#.*\n/g, "").replace(/[*_`[\]()]/g, "").trim();
  return text.length > length ? text.slice(0, length) + "..." : text;
}

export const collectionLabels: Record<string, string> = {
  papers: "Papers",
  logs: "Logs",
  experiments: "Experiments",
  audits: "Audits",
  literature: "Literature",
  rfes: "RFEs",
};

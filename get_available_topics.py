import os
import yaml

papers_dir = "content/papers"
all_papers = [f for f in os.listdir(papers_dir) if f.endswith('.md')]

already_written = [
  "mechanism-c-falsified",
  "observer-dependent-physics",
  "quantum-ceiling-debate",
  "quantum-framing-failure",
  "the-foliation-fallacy-debate",
  "the-proxy-ontology-fallacy",
  "the-quantum-ceiling",
  "the-scale-fallacy",
  "the-shrinking-illusion"
]

published = []
for filename in all_papers:
    filepath = os.path.join(papers_dir, filename)
    with open(filepath, "r") as f:
        content = f.read()
        if content.startswith("---"):
            try:
                end_idx = content.find("---", 3)
                if end_idx != -1:
                    frontmatter = yaml.safe_load(content[3:end_idx])
                    if frontmatter and frontmatter.get("status") == "published":
                        published.append(filename)
            except Exception as e:
                pass

print("Published papers:", published)

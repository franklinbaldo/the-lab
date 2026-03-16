import os
import yaml

papers_dir = "content/papers"
all_papers = [f for f in os.listdir(papers_dir) if f.endswith('.md')]

published = []
unpublished = []
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
                    else:
                        unpublished.append(filename)
            except Exception as e:
                pass

print("Unpublished papers:", unpublished[:10])

import os
import yaml

papers_dir = "content/papers"
published_papers = []

for filename in os.listdir(papers_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(papers_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
            if content.startswith("---"):
                try:
                    end_idx = content.find("---", 3)
                    if end_idx != -1:
                        frontmatter = yaml.safe_load(content[3:end_idx])
                        if frontmatter and frontmatter.get("status") == "published":
                            published_papers.append(filename)
                except Exception as e:
                    pass

print("Published papers:", published_papers)

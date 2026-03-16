import os
import yaml

articles_dir = "content/articles"
papers_dir = "content/papers"

covered_papers = set()
for filename in os.listdir(articles_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(articles_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
            if content.startswith("---"):
                try:
                    end_idx = content.find("---", 3)
                    if end_idx != -1:
                        frontmatter = yaml.safe_load(content[3:end_idx])
                        papers = frontmatter.get('papers', [])
                        if papers:
                            covered_papers.update(papers)
                except Exception as e:
                    pass

all_papers = set()
published = set()
for filename in os.listdir(papers_dir):
    if filename.endswith(".md"):
        all_papers.add(filename[:-3]) # strip .md
        filepath = os.path.join(papers_dir, filename)
        with open(filepath, "r") as f:
            content = f.read()
            if content.startswith("---"):
                try:
                    end_idx = content.find("---", 3)
                    if end_idx != -1:
                        frontmatter = yaml.safe_load(content[3:end_idx])
                        if frontmatter and frontmatter.get("status") == "published":
                            published.add(filename[:-3])
                except Exception as e:
                    pass


print(f"Total papers: {len(all_papers)}")
print(f"Covered papers: {len(covered_papers)}")
print(f"Published papers not covered: {published - covered_papers}")
print(f"Any paper not covered (first 20): {list(all_papers - covered_papers)[:20]}")

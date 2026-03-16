import os
import yaml

articles_dir = "content/articles"
all_articles = [f for f in os.listdir(articles_dir) if f.endswith('.md')]

for filename in all_articles:
    filepath = os.path.join(articles_dir, filename)
    with open(filepath, "r") as f:
        content = f.read()
        if content.startswith("---"):
            try:
                end_idx = content.find("---", 3)
                if end_idx != -1:
                    frontmatter = yaml.safe_load(content[3:end_idx])
                    print(f"{filename}: {frontmatter.get('title')}")
            except Exception as e:
                pass

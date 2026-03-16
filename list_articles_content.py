import os
import yaml

articles_dir = "content/articles"
all_articles = [f for f in os.listdir(articles_dir) if f.endswith('.md')]

for filename in all_articles:
    filepath = os.path.join(articles_dir, filename)
    with open(filepath, "r") as f:
        content = f.read()
        if "causal injection" in content.lower() or "pearl" in content.lower():
            print(f"{filename} contains causal/pearl references")

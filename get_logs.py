import os

logs_dir = "content/logs"
all_logs = []
for root, dirs, files in os.walk(logs_dir):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(root, f)
            all_logs.append(filepath)

print(f"Total logs: {len(all_logs)}")

# Find ones containing interesting keywords
interesting = []
for log in all_logs:
    with open(log, "r") as f:
        content = f.read()
        if "null result" in content.lower() or "surprising" in content.lower() or "disagree" in content.lower() or "controvers" in content.lower():
            interesting.append(log)

print("Interesting logs:", len(interesting))
for i in interesting[:10]:
    print(i)

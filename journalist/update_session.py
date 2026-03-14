import json

with open('journalist/session.json', 'r') as f:
    data = json.load(f)

if 'articles' not in data:
    data['articles'] = []

data['articles'].append('the-mechanism-c-contradiction')

with open('journalist/session.json', 'w') as f:
    json.dump(data, f, indent=2)

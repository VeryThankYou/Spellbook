import json

with open('data.json', 'r', encoding="utf-8") as f:
	data = json.load(f)
	f.close()

print(data[0]['slots'])

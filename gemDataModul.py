import json, requests

with open('data.json', 'r', encoding="utf-8") as f:
	data = json.load(f)
	f.close()

def prepSpell(string):
    response = requests.get("https://api.open5e.com/spells/?name="+str(string))
    result = json.load(response)
    print(str(result['results'][0]['desc']))

prepSpell("Acid Arrow")

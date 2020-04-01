import json, requests

with open('data.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
    f.close()

def prepSpell(string):
    response = requests.get("https://api.open5e.com/spells/?name="+str(string))
    response = response.json()
    data[0]['prep'].append(response['results'][0]['name'])
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()

def learnSpell(string):
    response = requests.get("https://api.open5e.com/spells/?name="+str(string))
    response = response.json()
    data[0]['know'].append(response['results'][0]['name'])
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()

prepSpell("Acid Arrow")



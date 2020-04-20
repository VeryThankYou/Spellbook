import json, requests

with open('data.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
    f.close()

def prepSpell(string):
    response = requests.get("https://api.open5e.com/spells/?search="+str(string))
    response = response.json()
    if len(response['results']) > 1:
        n = 1
        for e in response['results']:
            print(str(n)+" - "+str(e['name']))
            n += 1
        print("What spell did you mean?")
        inp = int(input("Choose spell by index number\n"))
        spellname = response['results'][inp-1]['name']
    else:
        spellname = response['results'][0]['name']
    known = 0
    for e in data[0]['prep']:
        if e == spellname:
            known += 1
    if known > 0:
        print("You have prepared this spell already.")
    else:
        data[0]['prep'].append(str(spellname))
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()



def learnSpell(string):
    response = requests.get("https://api.open5e.com/spells/?search="+str(string))
    response = response.json()
    if len(response['results']) > 1:
        n = 1
        for e in response['results']:
            print(str(n)+" - "+str(e['name']))
            n += 1
        print("What spell did you mean?")
        inp = int(input("Choose spell by index number\n"))
        spellname = response['results'][inp-1]['name']
    else:
        spellname = response['results'][0]['name']
    known = 0
    for e in data[0]['know']:
        if e == spellname:
            known += 1
    if known > 0:
        print("You have learned this spell already.")
    else:
        data[0]['know'].append(str(spellname))
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def lvlup():
    if int(data[0]['lvl']) >= 20:
        print("You are already at max level")
    else:
        data[0]['lvl'] = int(data[0]['lvl']) + 1
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def setlvl(i):
    if int(i) < 1 or int(i) > 20:
        print("Your input has to be within the level range 1-20")
    else:
        data[0]['lvl'] = int(i)
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def longRest():
    for e in data[0]['usedss']:
        data[0]['usedss'][e] = 0
    with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def useSpell(i):
    if data[0]['usedss'][str(i)] >= data[0]['maxss'][str(i)]:
        print("You have expended all spell slots of that level.")
    else:
        data[0]['usedss'][str(i)] = data[0]['usedss'][str(i)] + 1
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()    

def addSpellSlot(i):
    data[0]['maxss'][str(i)] += 1
    with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def setSpellSlot(i):
    numslot = input("How many spell slots of this level do you have?\n")
    data[0]['maxss'][str(i)] = int(numslot)
    with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def updateSpellSlots():
    with open('slotdata.json', 'r', encoding="utf-8") as f:
        wizdict = json.load(f)
        f.close()
    lvl = data[0]['lvl']
    tal = 1
    for e in wizdict[0][str(lvl)]:
        data[0]['maxss'][str(tal)] = wizdict[0][str(lvl)][e]
        tal += 1
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()

     

#prepSpell("Fireball")
#learnSpell("acid Arrow")
#learnSpell("eldri")
#lvlup()
setlvl(13)
#longRest()
#useSpell(1)
#addSpellSlot(3)
#setSpellSlot(3)
updateSpellSlots()
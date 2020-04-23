import json, requests
#Her importeres de biblioteker der bruges

def updateData():
    #Her defineres funktionen updateData som henter brugerens data fra den tilhørende json-fil og returnere den
    with open('data.json', 'r', encoding="utf-8") as f:
        #Først åbnes filen til læsning (grundet 'r'), som f
        data = json.load(f)
        f.close()
        #Nu gemmes indholdet i variablen data, og filen lukkes
    return data

def prepSpell():
    #Her defineres funktionen prepSpell, som tilføjer en spell til listen over prepared spells
    for e in data[charnumber]['know']:
        print(str(data[charnumber]['know'].index(e) + 1) + " - " + str(e) + "\n")
        #Først printes navnet på alle spells karakteren kender
    indx = int(input("Write the index number of the spell you want to prepare\n"))
    #Brugeren vælger den spell der skal prepareres
    try:
        spell = data[charnumber]['know'][indx-1]
        #Her gemmes navnet på den valgte spell. Dette gøres i en try-løkke så brugeren kan indtaste et forkert index uden at ødelægge programmet
        count = 0
        #Her oprettes en variabel der holder styr på om man har en spell med samme navn prepareret i forvejen
        for e in data[charnumber]['prep']:
            if e == spell:
                #For hvert element i listen over preparerede spells tjekkes om navnet er lig den valgte spell
                print("You have already prepared this spell")
                count += 1
                #I det tilfælde får brugeren at vide at de allerede har prepareret spellen, og der lægges 1 til count
        if count == 0:
            data[charnumber]['prep'].append(str(spell))
            #Hvis count stadig er lig 0, tilføjes den valgte spell til listen over preparerede spells i dataen
            with open('data.json', 'w', encoding="utf-8") as f:
                json.dump(data, f)
                f.close()
                #her gemmes dataen i data.json
            print(str(spell) + " has succesfully been prepared\n")
            #Brugeren får at vide at spellen er blevet prepareret
    except:
        answer = input("Invalid index number. Would you like to try again? (y/n)")
        #I except-delen får de at vide at der skete en index-fejl, og de bliver spurgt om de vil prøve igen
        if answer == "y":
            prepSpell()
            #Hvis de svarer ja, kaldes funktionen igen



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
    for e in data[charnumber]['know']:
        if e == spellname:
            known += 1
    if known > 0:
        print("You have learned this spell already.")
    else:
        data[charnumber]['know'].append(str(spellname))
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def lvlup():
    if int(data[charnumber]['lvl']) >= 20:
        print("You are already at max level")
    else:
        data[charnumber]['lvl'] = int(data[charnumber]['lvl']) + 1
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def setlvl(i):
    if int(i) < 1 or int(i) > 20:
        print("Your input has to be within the level range 1-20")
    else:
        data[charnumber]['lvl'] = int(i)
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def longRest():
    #Her defineres funktionen som nulstiller brugerens brugte spellslots
    for e in data[charnumber]['usedss']:
        data[charnumber]['usedss'][e] = 0
        #Her gennemgås listen over forskellige levels af spellslots, og de sættes alle til 0
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()
        #Her gemmes ændringerne i data.json


def useSpell(i):
    if data[charnumber]['usedss'][str(i)] >= data[charnumber]['maxss'][str(i)]:
        print("You have expended all spell slots of that level.")
    else:
        data[charnumber]['usedss'][str(i)] = data[charnumber]['usedss'][str(i)] + 1
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()    

def addSpellSlot():
    i = int(input("What level spellslot do you want to add?\n"))
    #Her defineres en funktion der tilføjer et spellslot af et specifikt level
    if i >= 1 and i <= 9:

        data[charnumber]['maxss'][str(i)] += 1

        with open('data.json', 'w', encoding="utf-8") as f:
                json.dump(data, f)
                f.close()
    else:
        print("Spellslots of that lvl doesn't exist\n")

def setSpellSlot(i):
    numslot = input("How many spell slots of this level do you have?\n")
    data[charnumber]['maxss'][str(i)] = int(numslot)
    with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()

def updateSpellSlots():
    with open('slotdata.json', 'r', encoding="utf-8") as f:
        wizdict = json.load(f)
        f.close()
    lvl = data[charnumber]['lvl']
    tal = 1
    for e in wizdict[0][str(lvl)]:
        data[charnumber]['maxss'][str(tal)] = wizdict[0][str(lvl)][e]
        tal += 1
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()

def addChar(name):
    with open('struktur.json', 'r', encoding="utf-8") as f:
        structure = json.load(f)
        f.close()
    structure[0]['name'] = name
    data.append(structure[0])
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()
    
def unprepSpell():
    for e in data[charnumber]['prep']:
        print(str(data[charnumber]['prep'].index(e) + 1) + " - " + str(e) + "\n")
    indx = int(input("Write the index number of the spell you want to remove from your prepared list\n"))
    try:
        del data[charnumber]['prep'][indx-1]
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()
    except:
        answer = input("Invalid index number. Would you like to try again? (y/n)")
        if answer == "y":
            unprepSpell()
        else:
            pass
    

     
data = updateData()
charnumber = 0
#learnSpell("acid Arrow")
#learnSpell("eldri")
#lvlup()
#setlvl(13)
#longRest()
#useSpell(1)
#addSpellSlot(3)
#setSpellSlot(3)
#updateSpellSlots()
learnSpell("delayed blast fire")
prepSpell()

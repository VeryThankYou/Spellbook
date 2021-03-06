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
    indx = input("Write the index number of the spell you want to prepare\n")
    #Brugeren vælger den spell der skal prepareres
    try:
        spell = data[charnumber]['know'][int(indx)-1]
        #Her gemmes navnet på den valgte spell. Dette gøres i en try-løkke så brugeren kan indtaste et forkert index uden at ødelægge programmet
        count = 0
        #Her oprettes en variabel der holder styr på om man har en spell med samme navn prepareret i forvejen
        for e in data[charnumber]['prep']:
            if e == spell:
                #For hvert element i listen over preparerede spells tjekkes om navnet er lig den valgte spell
                print("You have already prepared this spell\n")
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
        answer = input("Invalid index number. Would you like to try again? (y/n)\n")
        #I except-delen får de at vide at der skete en index-fejl, og de bliver spurgt om de vil prøve igen
        if answer == "y":
            prepSpell()
            #Hvis de svarer ja, kaldes funktionen igen



def learnSpell(string):
    #Her defineres en funktion der finder en spell fra api'en, og tilføjer det til listen over spells karakteren kender. Funktionen modtager parametret string, navnet på den spell man vil tilføje
    response = requests.get("https://api.open5e.com/spells/?search="+str(string))
    response = response.json()
    #Her søges på api'en efter inputtet, og api'ens response gemmes på json-format

    if len(response['results']) > 1:
        #Nu tjekkes om der er mere end et resultat fra søgningen
        n = 1
        #Her defineres en hjælpevariabel
        for e in response['results']:
            print(str(n)+" - "+str(e['name']))
            #Her printes alle resultater fra søgningen, med deres index-tal + 1 foran
            n += 1
            #Her lægges 1 til hjælpevariabel
        print("What spell did you mean?\n")
        inp = input("Choose spell by index number\n")
        #Her giver brugeren input om hvilket af resultaterne de ville lære
        try:
            spellname = response['results'][int(inp)-1]['name']
            #I try-klausulen prøves at gemme den valgte spells navn i variablen spellname
        except:
            print("Invalid index\n")
            #Hvis brugeren gav et forkert input, får de det at vide, og funktionen stoppes
            return
        #Her gemmes den valgte spells navn i variablen spellname
    elif len(response['results']) == 1:
        #Her tjekkes om der er et enkelt response
        answer = input("Do you want to learn the spell " + str(response['results'][0]['name']) + "? (y/n)\n")
        #Nu spørges brugeren om de vil lære den fundne spell
        if answer == "y":
            spellname = response['results'][0]['name']
            #Hvis svaret er ja, gemmes spellens navn i variablen spellname
        else:
            return
            #Funktionen stoppes
    else:
        print("No results\n")
        return
        #Hvis der ikke er nogen resultater for søgningen, får brugeren dette at vide, og funktionen stoppes
    known = 0
    #Hjælpevariabel der tæller om man kender en spell af samme navn
    for e in data[charnumber]['know']:
        if e == spellname:
            known += 1
            #For hver spell man kender, tjekkes om navnet er lig spellname, hvis det er lægges 1 til known
    if known > 0:
        print("You have learned this spell already.\n")
        #Hvis known er større end 0, får brugeren at vide at de allerede kender spellen
    else:
        data[charnumber]['know'].append(str(spellname))
        print("You have now learned " + str(spellname) + " successfully\n")
        #Ellers gemmes spellen i listen over kendte spells, og det printes at navnet på den valgte spell er gemt korrekt
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()
            #Her gemmes ændringerne i data.json

def lvlup():
    #Her defineres en funktion der tilføjer et level til ens karakter i dataen
    if int(data[charnumber]['lvl']) >= 20:
        print("You are already at max level\n")
        #Først tjekkes om karakteren er i max lvl. Hvis de er, får de dette at vide
    else:
        data[charnumber]['lvl'] = int(data[charnumber]['lvl']) + 1
        #Hvis ikke, lægges 1 til deres lvl i dataen
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()
            #Her gemmes ændringerne i data.json

def setlvl(i):
    #Her defineres en funktion der sætter karakterens level til et givent tal, nemlig parametret i
    try:
        if int(i) < 1 or int(i) > 20:
            print("Your input has to be within the level range 1-20\n")
            #Først tjekkes om i er mellem 1 og 20, da dette er lvl-intervallet i D&D, hvis ikke får brugeren dette at vide
        else:
            data[charnumber]['lvl'] = int(i)
            #Ellers sættes karakterens lvl til i i dataen
            with open('data.json', 'w', encoding="utf-8") as f:
                json.dump(data, f)
                f.close()
                #Her gemmes ændringerne i data.json
    except:
        print("Invalid input")

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
    #Her defineres en funktion der sætter tilføjer en brugt spellslot til dictionariet over brugte spellslots. Parametret i bestemmer hvilket lvl spellslot der bruges
    try:
        if data[charnumber]['usedss'][str(i)] >= data[charnumber]['maxss'][str(i)]:
            print("You have expended all spell slots of that level.\n")
            #Her tjekkes først om der er flere ubrugte spellslots af det valgte lvl
        else:
            data[charnumber]['usedss'][str(i)] = data[charnumber]['usedss'][str(i)] + 1
            #Hvis der er det, tillægges et brugt spellslot af det valgte lvl til dataen
            with open('data.json', 'w', encoding="utf-8") as f:
                json.dump(data, f)
                f.close()
                #Her gemmes dataen i data.json
    except:
        print("Invalid input\n")

def addSpellSlot():
    #Her defineres en funktion der tilføjer et spellslot af et specifikt level
    i = input("What level spellslot do you want to add?\n")
    #Her vælger brugeren hvilket lvl spellslot der skal tilføjes
    try:
        data[charnumber]['maxss'][str(i)] += 1
        #Her prøves at tilføje et ekstra spellslot af det valgte lvl
        with open('data.json', 'w', encoding="utf-8") as f:
                json.dump(data, f)
                f.close()
                #Her gemmes ændringerne i data.json
    except:
        print("Spellslots of that lvl doesn't exist\n")
        #Hvis lvl-inputtet var udfyldt forkert får brugeren det at vide

def setSpellSlot(i):
    #Her defineres en funktion der sætter antallet af spellslots af et specifikt level til i, parametret til funktionen
    numslot = input("How many spell slots of this level do you have?\n")
    #Her bedes brugeren om at skrive hvor mange spellslots af det level der skal være
    try:
        data[charnumber]['maxss'][str(i)] = int(numslot)
        #Her prøves at sætte mængden af spellslots til inputtet
        with open('data.json', 'w', encoding="utf-8") as f:
                json.dump(data, f)
                f.close()
                #Her gemmes ændringerne i data.json
    except:
        print("You didn't provide a number as an input\n")
        #Hvis lvl-inputtet var udfyldt forkert får brugeren det at vide

def updateSpellSlots():
    #Her defineres en feunktion der sætter karakterens spellslots til at passe til det lvl karakteren er i (fungerer kun for wizards)
    with open('slotdata.json', 'r', encoding="utf-8") as f:
        wizdict = json.load(f)
        f.close()
        #Først læses mængden af spellslots wizards har i sit lvl, og det gemmes i variablen wizdict som et dictionary
    lvl = data[charnumber]['lvl']
    tal = 1
    #Nu findes karakterens lvl i dataen og gemmes i en variabel, og hjælpevariablen tal oprettes
    for e in wizdict[0][str(lvl)]:
        #Her kører en for-løkke, der kører for hvert level af spellslots i det dictionary i wizdict der har index lig karakterens lvl
        data[charnumber]['maxss'][str(tal)] = wizdict[0][str(lvl)][e]
        tal += 1
        #Hver gennemkørsel af løkken sættes karakterens mængde af spellslots af det level løkken er på, til den mængde der er af de spellslots i wizdicts dictionary til karakterens lvl
        #Derudover lægges 1 til tal
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()
        #Her gemmes ændringerne i data.json

def addChar(name):
    #Her defineres en funktion som tilføjer en ekstra karakter til data.json. Funktionen modtager parametret name, som er navnet på den karakter der skal tilføjes
    with open('struktur.json', 'r', encoding="utf-8") as f:
        structure = json.load(f)
        f.close()
        #Her åbnes strukturen for det json-objekt der beskriver en karakter, og gemmes i en variabel
    structure[0]['name'] = name
    #Her sættes karakterens navn i struktur-variablen til parametret name. Bemærk at dette ikke gemmes i struktur.json, da denne skal indeholde den tomme struktur for en karakter
    data.append(structure[0])
    #Nu tilføjes json-elementet til dataen
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)
        f.close()
        #Her gemmes ændringerne i data.json

def unprepSpell():
    #Her defineres en funktion der kan fjerne spells fra listen over preparerede spells
    for e in data[charnumber]['prep']:
        print(str(data[charnumber]['prep'].index(e) + 1) + " - " + str(e) + "\n")
        #Her printen hver spell i listen, sammen med deres indexnummer + 1
    indx = input("Write the index number of the spell you want to remove from your prepared list\n")
    #Her giver brugeren et input med det viste indextal på sen spell der skal fjernes
    try:
        del data[charnumber]['prep'][int(indx)-1]
        #Her prøves at slette elementet i listen med det valgte index-nummer
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()
            #Her gemmes ændringerne i data.json
    except:
        answer = input("Invalid index number. Would you like to try again? (y/n)\n")
        #Hvis det var et ugyldigt index-nummer får brugeren dette at vide, og der spørges om funktionen skal kaldes igen
        if answer == "y":
            unprepSpell()
            #Hvis brugeren giver inputtet for ja, kaldes funktionen igen

def deleteCharacter():
    #Her defineres en funktion der kan fjerne karakterer fra datafilen
    for e in data:
        print(str(data.index(e) + 1) + " - " + str(e['name']) + "\n")
        #Her printen hver karakter i listen, sammen med deres indexnummer + 1
    indx = input("Write the index number of the character you want to delete\n")
    #Her giver brugeren et input med det viste indextal på den karakter der skal fjernes
    try:
        del data[int(indx)-1]
        #Her prøves at slette elementet i listen med det valgte index-nummer
        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f)
            f.close()
            #Her gemmes ændringerne i data.json
    except:
        answer = input("Invalid index number. Would you like to try again? (y/n)\n")
        #Hvis det var et ugyldigt index-nummer får brugeren dette at vide, og der spørges om funktionen skal kaldes igen
        if answer == "y":
            deleteCharacter()
            #Hvis brugeren giver inputtet for ja, kaldes funktionen igen

def regenSpellslot():
    #Her defineres en funktion der kan bruges til at regenerere enkelte spellslots, altså trække de fra listen over brugte spellslots i dataen
    for e in data[charnumber]["maxss"]:
        #Først kører en for-løkke for hvert lvl spellslot der findes
        print(str(e) + ". " + str(int(data[charnumber]["maxss"][e]) - int(data[charnumber]["usedss"][e])) + "/" + str(data[charnumber]["maxss"][e]))
        #Her printes hvilken mængde brugte og mulige spellslots brugeren har af dette level
    inp = input("What level spellslot do you want to regenerate?\n")
    #Her spørges om hvilket level spellslot der skal regenereres, svaret gemmes i en variabel
    try:
        #Her bruges en try- except-løkke, der kan fange om brugeren har givet ugyldigt input
        if data[charnumber]["usedss"][str(inp)] > 0:
            #Nu bruges en if-sætning til at tjekke om karakteren har brugte spellslots af det valgte level
            data[charnumber]["usedss"][str(inp)] -= 1
            #Hvis de har, trækkes et fra de brugte spellslots af det level
            with open('data.json', 'w', encoding="utf-8") as f:
                json.dump(data, f)
                f.close()
                #Her gemmes ændringerne i data.json
        else:
            print("You don't have a used spellslot of that level\n")
            #Hvis ikke der er nogen brugte spellslots af det level, får brugeren dette at vide
    except:
        print("Invalid input\n")
        #Hvis brugeren gav ugyldigt input, printes dette faktum



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
#learnSpell("blas")
# prepSpell()
#regenSpellslot()
#Hernede kaldtes funktioner under udvikling

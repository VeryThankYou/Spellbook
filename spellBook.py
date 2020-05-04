import apiStuff
import gemDataModul
import json
# Importerer et library og python filer

print('\nWelcome to Spellbook 720!!!1\n\n')
# Printer velkomst

def charSel():
# Definerer funktion til at lade brugeren vælge karakter og andre handlinger der ikke kræver en valgt karakter.
    print('\nYou need to select a character or create a new one to continue.')
    print(' - To search for a spell, write: "*[spell name]" (use 2 * for more info)')
    print(' - To select a character, write the number of the character.')
    print(' - To create a new character, write "+[Character name]"')
    print(' - To delete a character, write "-"')
    # Printer brugerens muligheder

    num = 0
    # Variabel til brug i for-løkke
    charData = gemDataModul.updateData()
    # Henter data om alle karaktere
    print("\nCharacters:")

    for i in charData:
        num = num + 1
        print(num, end = ". ")
        print(i.get("name"))
        # Print hver karakters navn samt et index. Der er også string manipulation

    answer = input("")
    # Lader brugeren give et input
    if answer[0] == "*":
        # Tjekker om det første element i string'en er et *
        if answer[1] == "*":
            # Tjekker om det andet element i string'en er et *
            apiStuff.findSpell(answer.replace("*",""), 1)
            charSel()
        else:
            apiStuff.findSpell(answer.replace("*",""), 0)
            charSel()
            # Søger efter besværgelse med ønskede mængde af detaljer.
            # Går derefter tilbage til forrige menu.

    elif answer[0] == "+":
        # Tjekker om det første element i string'en er et +
        gemDataModul.addChar(answer.replace("+",""))
        # Fjerner +'et og tilføjer en ny karakter
        charnumber = len(charData)
        # Deklarer charnumber til at være lige den lige den nye karakters index i listen over karaktere
        mainMenu(charnumber)
        # Går videre til næste menu

    elif answer[0] == "-":
        # Tjekker om det første element i string'en er et +
        gemDataModul.deleteCharacter()
        # Kalder deleteCharacter() funktionen
        charSel()
        # Går tilbage til tidligere menu

    elif answer.isnumeric() == True and int(answer) <= len(charData) and int(answer) > 0:
        # Tjekker om input'et er et tal, at det er mindre end mængden af karaktere, og at det er over 0
        charnumber = int(answer) - 1
        # Deklarer charnumber til at være lige valgte karakters index.
        mainMenu(charnumber)
        # Går videre til næste menu
    else:
        print("Input not understood. Please try again.")
        charSel()

def mainMenu(charNR):
# Definerer funktion til hovedmenuen. 1. argument er til at videre-/medbringe charnumber
    charnumber = charNR
    # Definerer charnumber til modtagne argument
    gemDataModul.charnumber = charnumber
    # Opdatere charnumber i gemDataModul.py
    charData = gemDataModul.updateData()
    # Deklarer charData til at være lige data om alle karaktere
    gemDataModul.data = charData
    # Opdatere data i gemDataModul.py

    print("\nHere you can use/search a spell, sleep, and level up!")
    print(' - To search for a spell, write: "*[spell name]" (use 2 * for more info)')
    print(' - To use a spell, write: "-[level of used spellslot]"')
    print(' - To sleep, write: "/sleep"')
    print(' - To view your spellbook, write: "/book"')
    print(' - To level up, write: "/lvlup"')
    print(' - To view you spellslots and level, write: "/info"')
    print(' - To regenerate a spellslot, write: "/regen"')
    print(' - To learn a spell, write: "+[spell name]"')
    # Printer hjælp til brugeren
    mAnswer = input("")
    # Lader brugeren svare
    if mAnswer[0] == "*":
        # Tjekker om det første element i string'en er et *
        if mAnswer[1] == "*":
            # Tjekker om det andet element i string'en er et *
            apiStuff.findSpell(mAnswer.replace("*",""), 1)
            mainMenu()
            # Søger efter besværgelse med ønskede mængde af detaljer.
            # Går derefter tilbage til forrige menu.
        else:
            apiStuff.findSpell(mAnswer.replace("*",""), 0)
            mainMenu()
            # Søger efter besværgelse med ønskede mængde af detaljer.
            # Går derefter tilbage til forrige menu.

    elif mAnswer[0] == "/":
        specAct = mAnswer.replace("/","")
        # Tjekker om det første element i string'en er et /. Hvis, sandt, fjerner /'et og gemmer det i specAct

        if specAct == "sleep":
            sleepz(charNR)
            # Hvis specAct er sleep, så gå til sleepz-menuen

        elif specAct == "lvlup":
            gemDataModul.lvlup()
            gemDataModul.updateSpellSlots()
            mainMenu(charnumber)
            # Hvis specAct er lvlup, så brug passende funktioner og gå tilbage til forrige menu.

        elif specAct == "book":
            # Tjekker om specAct er book
            cata = input('\nWould you like to view your prepared spells or known spells?\n1. Prepared\n2. Known\n')
            # Spørg bruger om ønskede list af besværgelse
            if cata == "1":
                for e in charData[charnumber].get("known"):
                    print(e)
                    # For hvert element i listen over kendte besværgelser, print besværgelsen

            elif cata == "2":
                for e in charData[charnumber].get("prep"):
                    print(e)
                    # For hvert element i listen over forberedte besværgelser, print besværgelsen
            mainMenu(charnumber)
            # Gå tilbage til hovedmenuen

        elif specAct == "info":
            # Tjekker om specAct er book
            print(charData[charnumber].get("name") + ' is level ', end="")
            print(charData[charnumber].get("lvl"))
            # Printer navn og level på karakter
            for e in charData[charnumber].get("maxss"):
                print(e, end=". ")
                print(int(charData[charnumber].get("maxss").get(e)) - int(charData[charnumber].get("usedss").get(e)), end="/")
                print(charData[charnumber].get("maxss").get(e))
                # For hvert element i dictionary'en over max-spellslots, print hvor mange der er tilbage af hvert level.
            mainMenu(charnumber)
            # Gå tilbage til hovedmenuen

        elif specAct == "regen":
            # Tjekker om specAct er regen
            gemDataModul.regenSpellslot()
            # Kører regenSpellslot funktionen
            mainMenu(charnumber)
            # Går tilbage til hovedmenuen

        else:
            print("Input not understood. Please try again.")
            mainMenu(charnumber)
            # Hvis inputet ikke passede nogen if-statement, lad brugeren prøve igen.

    elif mAnswer[0] == "-" and mAnswer.replace("-","").isnumeric() == True and mAnswer.replace("-","").isnumeric() != 0 and mAnswer.replace("-","").isnumeric() <= 9:
        # Tjekker om det første element i string'en er et -, og at der er et tal mellem 1 og 9
        uSpell = mAnswer.replace("-","")
        # Fjerne -'et og gemmer det i uSpell
        gemDataModul.useSpell(uSpell)
        # Kører useSpell funktionen
        mainMenu(charnumber)
        # Går tilbage til hovedmenuen

    elif mAnswer[0] == "+":
        # Tjekker om det første element i string'en er et +
        gemDataModul.learnSpell(mAnswer.replace("+",""))
        # Kører learnSpell funktionen
        mainMenu(charnumber)
        # Går tilbage til hovedmenuen

    else:
        print("Input not understood. Please try again.")
        mainMenu(charnumber)
        # Hvis inputet ikke passede nogen if-statement, lad brugeren prøve igen.


def sleepz(charNR):
# definere funktion til at
    charData = gemDataModul.updateData()
    gemDataModul.data = charData
    # Opdatere og gemmer data om karaktere

    print('\nHere you can prepare and "unprepare" spells')
    print(' - To prepare a spell, write /prep.')
    print(' - To "unprepare" a spell, write /unprep.')
    print(' - To "wake up", write /wake.')
    sAnswer = input('')
    # Printer hjælp til brugeren og lader dem svare

    if sAnswer[0] == "/":
        # Tjekker om det første element i string'en er et /
        sleepAct = sAnswer.replace("/","")
        # Fjerner /'et og gemmer det i sleepAct
        if sleepAct == "prep":
            gemDataModul.prepSpell()
            sleepz(charNR)
            # Hvis sleepAct er "prep", kør prepSpell-funktionen og gå tilbage til sleep-menuen

        elif sleepAct == "unprep":
            gemDataModul.unprepSpell()
            sleepz(charNR)
            # Hvis sleepAct er "unprep", kør unprepSpell-funktionen og gå tilbage til sleep-menuen

        elif sleepAct == "wake":
            mainMenu(charNR)
            # Hvis sleepAct er "wake", gå tilbage til hovedmenuen

        else:
            print("Input not understood. Please try again.")
            sleepz(charNR)
            # Hvis inputet ikke passede nogen if-statement, lad brugeren prøve igen.

    else:
        print("Input not understood. Please try again.")
        sleepz(charNR)
        # Hvis inputet ikke passede nogen if-statement, lad brugeren prøve igen.


charSel()
# Kør dene første menu.

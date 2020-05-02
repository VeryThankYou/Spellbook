import apiStuff
import gemDataModul
import json

print('\nWelcome to Spellbook 720!!!1\n\n')

def charSel():

    print('\nYou need to select a character or create a new one to continue.')
    print(' - To search for a spell, write: "*[spell name]" (use 2 * for more info)')
    print(' - To select a character, write the number of the character.')
    print(' - To create a new character, write "+[Character name]"')
    print(' - To delete a character, write "-"')

    num = 0
    charData = gemDataModul.updateData()
    print("\nCharacters:")
    for i in charData:
        num = num + 1
        print(num, end = ". ")
        print(i.get("name"))

    answer = input("")
    if answer[0] == "*":
        if answer[1] == "*":
            apiStuff.findSpell(answer.replace("*",""), 1)
            charSel()
        else:
            apiStuff.findSpell(answer.replace("*",""), 0)
            charSel()
    elif answer[0] == "+":
        gemDataModul.addChar(answer.replace("+",""))
        charnumber = len(charData) - 1
        mainMenu()
    elif answer[0] == "-":
        gemDataModul.deleteCharacter()
        charSel()
    elif answer.isnumeric() == True and int(answer) <= len(charData) and int(answer) > 0:
        charnumber = int(answer) - 1
        mainMenu()
    else:
        print("nope, prøv igen, kammerat")
        charSel()

def mainMenu():

    charData = gemDataModul.updateData()
    print("\nHere you can use/search a spell, sleep, and level up!")
    print(' - To search for a spell, write: "*[spell name]" (use 2 * for more info)')
    print(' - To use a spell, write: "-[level of used spellslot]"')
    print(' - To sleep, write: "/sleep"')
    print(' - To view your spellbook, write: "/view"')
    print(' - To level up, write: "/lvlup"')
    print(' - To learn a spell, write: "+[spell name]"')
    mAnswer = input("")
    if mAnswer[0] == "*":
        apiStuff.findSpell(mAnswer.replace("*",""))
        mainMenu()
    elif mAnswer[0] == "/":
        specAct = mAnswer.replace("/","")

        if specAct == "sleep":
            gemDataModul.longRest()
            gemDataModul.prepSpell()
            gemDataModul.unprepSpell()
            mainMenu()

        elif specAct == "lvlup":
            gemDataModul.lvlup()
            gemDataModul.updateSpellSlots()
            mainMenu()

        elif specAct == "view":
            cata = input('\nWould you like to view your know spells or prepared spells?\n1. Know\n2. Prepared\n')
            if cata == "1":
                for e in charData[charnumber]:
                    print(e)
            elif cata == "2":
                for e in charData[charnumber]:
                    print(e)
            mainMenu()

        else:
            print("Please write an actual function")
            mainMenu()

    elif mAnswer[0] == "-":
        uSpell = mAnswer.replace("-","")
        gemDataModul.useSpell(uSpell)
        mainMenu()

    elif mAnswer[0] == "+":
        gemDataModul.learnSpell(mAnswer.replace("+",""))
        mainMenu()

    else:
        print("try again")
        mainMenu()

charSel()

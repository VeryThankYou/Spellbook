import apiStuff
import gemDataModul
import json

print('\nWelcome to Spellbook 720!!!1\n\n - You can, at any time, write "*[spell name]" to search for a spell.')
charAns = None

def charSel():

    print('\nWrite the name of the character you wish to select, or "+[Character name]" to create a new one.')
    num = 0
    charData = gemDataModul.updateData()
    for i in charData:
        num = num + 1
        print(num, end = ". ")
        print(i.get("name"))

    answer = input("")
    if answer[0] == "*":
        apiStuff.findSpell(answer.replace("*",""))
        charSel()
    elif answer[0] == "+":
        gemDataModul.addChar(answer.replace("+",""))
        charnumber = len(charData) - 1
        mainMenu()
    else:
        try:
            if int(answer) <= len(charData):
                charnumber = int(answer) - 1
                mainMenu()
        except:
            print("nope, prøv igen, kammerat")
            charSel()

def mainMenu():

    charData = gemDataModul.updateData()
    print("Here you can use/search a spell, sleep, and level up!\n")
    print(' - To search for a spell, write: "*[spell name]"')
    print(' - To use a spell, write: "-[level of used spellslot]"')
    print(' - To sleep, write: "+sleep"')
    print(' - To level up, write: "+lvlup"')
    print(' - To learn a spell, write: "+[spell name]"')
    mAnswer = input("")
    if mAnswer[0] == "*":
        apiStuff.findSpell(mAnswer.replace("*",""))
    elif mAnswer[0] == "+":
        specAct = mAnswer.replace("+","")
        if specAct == "sleep":
            gemDataModul.longRest()
            gemDataModul.prepSpell()
            gemDataModul.unprepSpell()
            mainMenu()
        elif specAct == "lvlup":
            gemDataModul.lvlup()
            gemDataModul.updateSpellSlots()
            mainMenu()
        else:
            print("Please write an actual function")
    elif mAnswer[0] == "-":
        uSpell = mAnswer.replace("-","")
        gemDataModul.useSpell(uSpell)
        mainMenu()
    elif mAnswer[0] == "/":
        gemDataModul.learnSpell(mAnswer.replace("/",""))
    else:
        print("try again")

charSel()

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
    elif answer[0] == "+":
        gemDataModul.addChar(answer.replace("+",""))
    else:
        try:
            if int(answer) <= len(charData):
                charNum = int(answer) - 1
        except:
            print("nope, prøv igen, kammerat")

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
        elif specAct == "lvlup":
            gemDataModul.lvlup()
            gemDataModul.updateSpellSlots()
        else:
            print("Please write an actual function")
    elif mAnswer[0] == "-":
        uSpell = mAnswer.replace("-","")
        gemDataModul.useSpell(uSpell)
    elif mAnswer[0] == "/":
        gemDataModul.learnSpell(mAnswer.replace("/",""))
    else:
        print("try again")

charnumber = 0
mainMenu()

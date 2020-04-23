import apiStuff
import gemDataModul
import json

print('\nWelcome to Spellbook 720!!!1\n\n - You can, at any time, write "*[spell name]" to search for a spell.')
charNum = None

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


charSel()

import apiStuff
import gemDataModul
import json

print('\nWelcome to Spellbook 720!!!1\n\n - You can, at any time, write "*[spell name]" to search for a spell.')


def charSel():

    print('\nWrite the name of the character you wish to select, or "+[Character name]" to create a new one.')
    num = 0
    for i in gemDataModul.updateData():
        num = num + 1
        print(num, end = ". ")
        print(i.get("name"))

    Answer = input("")
    if Answer[0] == "*":
        apiStuff.findSpell(Answer.replace("*",""))
        print("Answer.replace("*","")")
    elif Answer[0] == "+":
        gemDataModul.addChar(Answer.replace("+",""))
    else:
        try:
            for i in gemDataModul.updateData():
                if charName =
        ex
        print("We are number one!")


charSel()

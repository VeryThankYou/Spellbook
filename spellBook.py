import apiStuff

print('\nWelcome to Spellbook 720!!!1\n - You can, at any time, write "*[spell name]" to search for a spell.')
Answer = input("skrt")

def intro():
    if Answer[0] == "*":
        apiStuff.findSpell(Answer.replace("*",""))
        print("Answer.replace("*","")")
    else:
        print("We are number one!")




intro()

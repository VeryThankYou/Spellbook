import json


# with open("spells.json", "r", encoding="utf-8") as json_file:
#     data = json.load(json_file)

def findSpell():
    searchedSpell = input("Which spell do you want to find? \n")
    spellName = searchedSpell.lower()
    spellName = spellName.title()

    if spellName in data.keys():
        return data[spellName]

    else:
        spellName = searchedSpell.replace(" ","")
        spellName = spellName.lower()
        spellName = spellName.title()
        if spellName in data.keys():
            return data[spellName]


print(findSpell())
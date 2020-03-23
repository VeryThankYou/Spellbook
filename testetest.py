import json
import requests


response = requests.get("api.open5e.com/spells/?dnd_class=Wizard")

print(response)



# def findSpell():
#     searchedSpell = input("Which spell do you want to find? \n")
#     spellName = searchedSpell.lower()
#     spellName = spellName.title()

#     if spellName in data.keys():
#         return data[spellName]

#     else:
#         spellName = searchedSpell.replace(" ","")
#         spellName = spellName.lower()
#         spellName = spellName.title()
#         if spellName in data.keys():
#             return data[spellName]


# print(findSpell())
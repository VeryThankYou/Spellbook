import json
import requests


searchThis = input("Hvilken besværgelse vil du gerne finde?\n")
response = requests.get("https://api.open5e.com/spells/?search="+searchThis)

print(response)
if response.status_code == 200:
    ting1 = response.text
    print(ting1)





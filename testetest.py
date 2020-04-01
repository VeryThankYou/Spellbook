import json
import requests


searchThis = input("Hvilken besværgelse vil du gerne finde?\n")
response = requests.get("https://api.open5e.com/spells/?search="+searchThis)

print(response)
if response.status_code == 200:
    meem = response.text
    dic = json.loads(meem)
    dic2 = dic.get("results")
    if dic.get("count") > 1 and dic.get("count") < 11:
        spelz = []
        for e in dic2:
            spelz.append(e.get("name"))
        for e in range(len(spelz)):
            num = e+1
            print(num, end = ". ")
            print(spelz[e])
        ans = int(input("Which of these spells is l00k 4?\n" ))
        print(spelz[ans])

    elif dic.get("count") == 1:
        lul = dic2[0]
        print(lul.get("name"))

    elif dic.get("count") == 0:
        print("There are no spellzzz with this naeem\n")
        
    else:
        print("2 manyy spelzz braj, be spesifig, dyd\n")


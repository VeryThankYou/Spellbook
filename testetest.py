import json
import requests

def tranScribe(spelStuff):
    for e in spelStuff:
        print(e, end = "")
        mRum = 24 - len(e)
        for i in range(mRum):
            print(" ", end = "")
        print(":    ", end = "")

        print(spelStuff.get(e))

def findSpell():
    searchThis = input("Hvilken besværgelse vil du gerne finde?\n")
    response = requests.get("https://api.open5e.com/spells/?search="+searchThis)
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
            tranScribe(dic2[ans - 1])

        elif dic.get("count") == 1:
            lul = dic2[0]
            tranScribe(lul)

        elif dic.get("count") == 0:
            print("There are no spellzzz with this naeem\n")

        else:
            print("2 manyy spelzz braj, be spesifig, dyd\n")
    else:
        print("OOPSIE WOOPSE!! Uwu You made a fuckie wuckie!! A wittle fucko boingo! The code monkeys at our headquarteres are working VEWY HAWD to fix this! JK do it yourself")
        print(response.status_code)

findSpell()
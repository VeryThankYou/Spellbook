import json
import requests

def tranScribe(spelStuff, detail = 0):
    for e in spelStuff:
        if detail == 0:
            if e == "archetype" or e == "dnd_class" or e == "school" or e == "circles" or e == "page" or e == "slug" or e == "level_int" or e == "document__slug" or e == "document__title" or e == "document__license_url":
                continue
        elif detail == 1:
            if e == "slug" or e == "level_int" or e == "document__slug" or e == "document__title" or e == "document__license_url":
                continue

        elif e == "desc":
            print("Description", end = "")
            print("     :    ", end = "")
            print(". ".join(i.capitalize() for i in spelStuff.get(e).split(". ")))

        print(e.capitalize().replace("_", " "), end = "")
        mRum = 16 - len(e)
        for i in range(mRum):
            print(" ", end = "")
        print(":    ", end = "")
        print(spelStuff.get(e).capitalize().replace("<br/>",", "))

def findSpell(preDef = "***", detail = 0):

    if preDef == "***":
        searchThis = input("Hvilken besværgelse vil du gerne finde?\n")
    else:
        searchThis = preDef

    response = requests.get("https://api.open5e.com/spells/?search="+searchThis)

    if response.status_code == 200:
        resp = response.text
        dic = json.loads(resp)
        dic2 = dic.get("results")

        if dic.get("count") > 1 and dic.get("count") < 11:
            spelz = []
            for e in dic2:
                spelz.append(e.get("name"))
            print("\nTo select a spell, write its number.")
            for e in range(len(spelz)):
                num = e+1
                print(num, end = ". ")
                print(spelz[e])

            ans = int(input(""))
            tranScribe(dic2[ans - 1], detail)

        elif dic.get("count") == 1:
            ans1 = dic2[0]
            tranScribe(ans1, detail)

        elif dic.get("count") == 0:
            print("There are no spellzzz with this naeem\n")

        else:
            print("2 manyy spelzz braj, be spesifig, dyd\n")
    else:
        print("OOPSIE WOOPSE!! Uwu You made a fuckie wuckie!! A wittle fucko boingo! The code monkeys at our headquarteres are working VEWY HAWD to fix this! JK do it yourself, lol")
        print(response.status_code)

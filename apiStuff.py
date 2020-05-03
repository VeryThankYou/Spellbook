import json
import requests
# Importerer libraries

def tranScribe(spelStuff, detail = 0):
    # Definerer funktion til at printe besværgelser. 1. argument er besværgelsens dictionary. 2. argument til ønsket om meget eller lidt information
    for e in range(20):
        print("-", end="")
        # For-løkke til at visuel opdeling
    print("")
    # Print til at gå ned på næste linje
    for e in spelStuff:
        # Går igennem hvert element i besværgelsens dictionary.
        if detail == 0:
            # Tjekker om der er ønsket lidt information. Dette er standard
            if e == "archetype" or e == "dnd_class" or e == "school" or e == "circles" or e == "page" or e == "slug" or e == "level_int" or e == "document__slug" or e == "document__title" or e == "document__license_url":
                continue
                # Nogle elementer ønsker vi ikke at printe. Disse linje springer videre til næste element i løkken, når de uønskede elementer kommer

        elif detail == 1:
            # Tjekker om der er ønsket meget information.
            if e == "slug" or e == "level_int" or e == "document__slug" or e == "document__title" or e == "document__license_url":
                continue
                # Samme som sidste if-sætning. Denne gang er der færre uønskede elementer

        elif e == "desc":
            print("Description", end = "")
            print("     :    ", end = "")
            print(". ".join(i.capitalize() for i in spelStuff.get(e).split(". ")))
            # Printer desc elementet pænere end det står i dictionary'en

        print(e.capitalize().replace("_", " "), end = "")
        mRum = 16 - len(e)
        for i in range(mRum):
            print(" ", end = "")
        print(":    ", end = "")
        print(spelStuff.get(e).capitalize().replace("<br/>",", "))
        # Manipulerer string for at gøre dem pænere. Sikre at teksten er lodret opstillet

    for e in range(20):
        print("-", end="")
        # Visuel overblik

def findSpell(preDef = "***", detail = 0):
    # Definerer funktion til at finde en besværgelse. 1. argument tillader at funktionen modtager besværgelsens navn, men funktionen fungerer uden. 2. argument er ønskede niveau af detaljer

    if preDef == "***":
        searchThis = input("Hvilken besværgelse vil du gerne finde?\n")
        # Hvis funktionen ikke modtog et navn på en besværgelse bliver man spurgt om det her
    else:
        searchThis = preDef
        # Hvis funktionen modtog et navn på en besværgelse
    response = requests.get("https://api.open5e.com/spells/?search="+searchThis)
        # Søger efter besværgelsen inden på API'en

    if response.status_code == 200:
        resp = response.text
        dic = json.loads(resp)
        dic2 = dic.get("results")
        # "Grav" ned i modtagne data for at finde listen af besværgelse med det søgte i navnet.

        if dic.get("count") > 1 and dic.get("count") < 11:
            # Hvis mellem 2 og 10 besværgelser matchede det søgte
            spelz = []
            for e in dic2:
                spelz.append(e.get("name"))
                # Tilføjer de matchende navne til en liste
            print("\nTo select a spell, write its number.")
            for e in range(len(spelz)):
                num = e+1
                print(num, end = ". ")
                print(spelz[e])
                # For-løkke til at printe alle besværgelser der matchede

            ans = int(input(""))
            # Input så brugeren kan vælge hvilken besværgelse de øsnker
            tranScribe(dic2[ans - 1], detail)
            # Udskriver valgte besværgelse

        elif dic.get("count") == 1:
            ans1 = dic2[0]
            tranScribe(ans1, detail)
            # Hvis der kun er en matchende besværgelse bliver den printet.

        elif dic.get("count") == 0:
            print("There are no spells with this name.\n")
            # Hvis der ikke er nogle matchende besværgelser

        else:
            print("Too many spells fit your search.\n")
            # Hvis der er for mange matchende besværgelse. Dog kan denne else-statement også nås ved andre fejl, men i de tilfælde vil der typisk være 0 matchende besværgelser
    else:
        print("Search failed", end="")
        print(response.status_code)
        # Hvis der ikke bliver skabt forbindelse til API'en

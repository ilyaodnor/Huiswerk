antwoord = ""
while True:
    antwoord = input("Wat is uw antwoord: Ja of Nee").lower()
    if antwoord in ("ja", "nee"):
        if antwoord == 'ja':
            antwoord = True
        elif antwoord == 'nee':
            antwoord = False

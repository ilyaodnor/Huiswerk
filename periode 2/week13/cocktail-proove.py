cocktails = [
    {"name": "Mojito", "alcohol": True, "taste": "fresh", "fruit": True, "price": 8},
    {"name": "Martini", "alcohol": True, "taste": "dry", "fruit": False, "price": 10},
    {"name": "Piña Colada", "alcohol": True, "taste": "sweet", "fruit": True, "price": 12},
    {"name": "Daiquiri", "alcohol": True, "taste": "sour", "fruit": True, "price": 9},
    {"name": "Virgin Mojito", "alcohol": False, "taste": "fresh", "fruit": True, "price": 5},
    {"name": "Lemonade", "alcohol": False, "taste": "sweet", "fruit": False, "price": 4},
    {"name": "Bloody Mary", "alcohol": True, "taste": "spicy", "fruit": False, "price": 11},
    {"name": "Tequila Sunrise", "alcohol": True, "taste": "sweet", "fruit": True, "price": 10}
]
def vraag(vraag):
    while True:
        antwoord = input(vraag).lower()
        if antwoord == 'ja' or antwoord == 'nee':
            return antwoord
        else:
            print('Voer in ja of nee!!')


alcohol = vraag("Heeft jouw drank alkoohol? ")

if alcohol == 'ja':
    for cocktail in cocktails:
        if cocktail['alcohol'] == False:
            cocktails.remove(cocktail)
elif alcohol == 'nee':
    for cocktail in cocktails:
        if cocktail['alcohol'] == True:
            cocktails.remove(cocktail)


smaaken = ['dry', 'fresh', 'sweet','sour','spicy']

while True:
    smaak = input('Welke smaak heeft het? (dry, fresh, sweet, sour, spicy) ').lower()
    if smaak in smaaken:
        cocktails = [cocktail for cocktail in cocktails if cocktail['taste'] == smaak]
        break
    else:
        print('Voer een geldige smaak in!!')
print(cocktails)

fruit = vraag('Heeft youw drank fruiten? ')
if fruit == 'ja':
    for cocktail in cocktails:
        if cocktail['fruit'] == False:
            cocktails.remove(cocktail)
elif fruit == 'nee':
    for cocktail in cocktails:
        if cocktail['fruit'] == True:
            cocktails.remove(cocktail)


kost = int(input('Hoeveel kost het? '))
cocktails = [cocktail for cocktail in cocktails if cocktail['price'] == kost]

if len(cocktails) == 0:
    print('Geen cocktails gevonden die aan jouw voorkeuren voldoen.')
elif len(cocktails) == 1:
    print(f'{cocktails['name']} is jouw cocktail.')
else:
    cocktails_namen = []
    for i in cocktails: 
        cocktails_namen.append(i['name'])
    print(f'{' '.join(cocktails_namen)} past bij uw beschrijving.')
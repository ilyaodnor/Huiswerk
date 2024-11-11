lijst = [5,12,19,27,3]
lijst.append(25)
print(lijst)
print(f'Er zitten {len(lijst)} elementen in de lijst.')
lijst.remove(lijst[1])
cijfer = lijst.pop(0)
print(f'Het nummer {cijfer} is verwijderd')
print(f'Het totaal van de lijst is {sum(lijst)}')
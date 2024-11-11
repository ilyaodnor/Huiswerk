def bereken_poten(giraffen,zebras,vogels):
    return f'ze hebben totaal {giraffen*4+zebras*4+vogels*2} poten. '
a = int(input('hoeveel giraffen? '))
b = int(input('hoeveel zebra\'s? '))
c = int(input('hoeveel vogels? '))

print(bereken_poten(a,b,c))
getallen = []
for i in range(10):
    while True:
        try:
            a = int(input('Voer in een cijfer:'))
            break
        except ValueError:
            print('je moet een cijfer voeren!! ')
        
    getallen.append(a)
getallen
deelbaar = []
for i in getallen:
    if i%3 ==0 and i not in deelbaar:
        deelbaar.append(i)
print(f'het grootste getal is: {max(getallen)}')
print(f'het kleinste getal is: {min(getallen)}')
result = ' '.join(map(str, deelbaar))
if len(deelbaar)>0:
    print(f'het aantal getallen deelbaar door 3 (zonder rest) is: {result}')

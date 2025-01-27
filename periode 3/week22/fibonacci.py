def fibonacci_getallen():
    getal_1 = int(input('Van welk getal wilt u de tafel zien:'))
    getal_2 = int(input('Voer in twede getaal: '))
    fibonacci_lijst = [getal_1,getal_2]
    
    for i in range(9):
        fibonacci_lijst.append(fibonacci_lijst[i+1]+fibonacci_lijst[i])
    
    print(', '.join(map(str,fibonacci_lijst)))
fibonacci_getallen()
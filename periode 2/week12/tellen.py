a = int(input('Voer in integer: '))
if a > 0:
    for i in range(a,-1,-1):
        print(i)
elif a<0:
    for i in range(a,1):
        print(i)
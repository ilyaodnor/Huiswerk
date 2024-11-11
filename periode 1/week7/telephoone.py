
iphone_prijs = int(input('Voer in prijs voor iPhone: '))
samsung_prijs = int(input('Voer in prijs voor Samsung: '))
asus_prijs = int(input('Voer in prijs voor Asus: '))

maximum = max(iphone_prijs, samsung_prijs, asus_prijs)
middel = iphone_prijs + samsung_prijs + asus_prijs - min(iphone_prijs, samsung_prijs, asus_prijs) - max(iphone_prijs, samsung_prijs, asus_prijs)
minimum = min(iphone_prijs, samsung_prijs, asus_prijs)


if iphone_prijs < 900 and samsung_prijs < 900 and asus_prijs < 900:

    if samsung_prijs - asus_prijs > 100 and iphone_prijs - asus_prijs > 100:
        if maximum == iphone_prijs:
            print(f'De iPhone is het duurst, de telefoon kost: {maximum} Euro')
        elif maximum == samsung_prijs:
            print(f'De Samsung is het duurst, de telefoon kost: {maximum} Euro')
        elif maximum == asus_prijs:
            print(f'De Asus is het duurst, de telefoon kost: {maximum} Euro')

    elif iphone_prijs > samsung_prijs:
        print(f'De iPhone is het duurst, de telefoon kost: {iphone_prijs} Euro')
        print(f'De Samsung is het goedkoopst, de telefoon kost: {samsung_prijs} Euro')
        if iphone_prijs - samsung_prijs < 50:
            print('Het advies is dus de iPhone te kopen.')
        else:
            print('Het advies is dus de Samsung te kopen.')

    elif iphone_prijs < samsung_prijs:
        print(f'De Samsung is het duurst, de telefoon kost: {samsung_prijs} Euro')
        print(f'De iPhone is het goedkoopst, de telefoon kost: {iphone_prijs} Euro')
        if samsung_prijs - iphone_prijs < 50:
            print('Het advies is dus de Samsung te kopen.')
        else:
            print('Het advies is dus de iPhone te kopen.')

else:
    print('Het advies is dus geen telefoon te kopen, ze zijn te duur.')

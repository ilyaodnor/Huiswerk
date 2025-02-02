Look_and_Say = ['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211','31131211131221','13211311123113112211','11131221133112132113212221']


def logic(vorige_getal):
    new_getal = ''
    i = 0

    while i < len(vorige_getal):
        count = 1  
        while i + 1 < len(vorige_getal) and vorige_getal[i] == vorige_getal[i + 1]:
            count += 1
            i += 1  
        
        new_getal += str(count) + vorige_getal[i] 
        i += 1  

    return new_getal

getal = '1'
for i in Look_and_Say:
    if i == Look_and_Say[0]:
        print(getal + '==' + i )
        print( getal == i)
    else:
        getal = logic(getal)
        print(getal + '== ' + i )
        print( getal == i)



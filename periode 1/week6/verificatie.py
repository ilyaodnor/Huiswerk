import math
burgerschap = False

engels = round(float(input('Welke cijfer hebt u voor engels examen?')))
if engels >=5:
    engels = True


nederlands = round(float(input('Welke cijfer hebt u voor Nederlands examen?')))
if nederlands >=4:
    nederlands = True

rekenen= round(float(input('Welke cijfer hebt u voor Nederlands examen?')))
if rekenen >=4:
    rekenen = True

dev_skills = round(float(input('Welke cijfer hebt u voor Nederlands examen?')))
if dev_skills >=4:
    dev_skills = True

gemiddeld = []
for i in range(4):
    gemiddeld.append(round(float(input('''Welke cijfers hebt u voor:          -de politiek-juridische dimensie
                                                                        -de economische dimensie
                                                                        -de maatschappelijk-sociale dimensie
                                                                        -de dimensie vitaal burgerschap.'''))))
summa = sum(gemiddeld)/4
if summa >= 6:
    burgerschap = True



if all([engels, nederlands, rekenen, dev_skills, burgerschap]):
    print('Je haal een diploma')
else:
    print('Je hebt niet genoeg scoren. Je haal geen diploma.')
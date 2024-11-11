import math
burgerschap = False
def get_letter_grade(score):
    if 8.5 <= score <= 10:
        return 'A'
    elif 7.5 <= score < 8.5:
        return 'B'
    elif 6.5 <= score < 7.5:
        return 'C'
    elif 5.5 <= score < 6.5:
        return 'D'
    elif 0 <= score < 5.5:
        return 'F'
    else:
        return 'Invalid score'


engels = round(float(input('Welke cijfer hebt u voor engels examen?')))
engels =get_letter_grade(engels)



nederlands = round(float(input('Welke cijfer hebt u voor Nederlands examen?')))
nederlands =get_letter_grade(nederlands)

rekenen= round(float(input('Welke cijfer hebt u voor Nederlands examen?')))
rekenen =get_letter_grade(rekenen)

dev_skills = round(float(input('Welke cijfer hebt u voor Nederlands examen?')))
dev_skills =get_letter_grade(dev_skills)

gemiddeld = []
for i in range(4):
    gemiddeld.append(round(float(input('''Welke cijfers hebt u voor:          -de politiek-juridische dimensie
                                                                        -de economische dimensie
                                                                        -de maatschappelijk-sociale dimensie
                                                                        -de dimensie vitaal burgerschap.'''))))
summa = sum(gemiddeld)/4
summa =get_letter_grade(summa)



if engels!='F' and nederlands!='F' and rekenen!='F' and dev_skills!='F' and summa!='F':
    print('Je haal een diploma')
    print(f'''
engels: {engels}
nederlands: {nederlands}
rekenen: {rekenen}
dev_skills: {dev_skills}
burgerschap: {summa}
          ''')
else:
    print('Je hebt niet genoeg scoren. Je haal geen diploma.')
    print(f'''
engels: {engels}
nederlands: {nederlands}
rekenen: {rekenen}
dev_skills: {dev_skills}
burgerschap: {summa}
          ''')

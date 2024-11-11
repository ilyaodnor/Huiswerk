while True:      
    word_1 = input('Woer in een word: ')
    if len(word_1.split())>0:
        break
    else:
        print('Voer in een word!!')

while True:      
    word_2 = input('Woer in een word: ')
    if len(word_2.split())>0:
        break
    else:
        print('Voer in een word!!')

letters = []
for letter in word_1:
    for i in word_2:
        if letter == i:
            letters.append(letter)
if len(letters) == 0:
    print('Die worden hebben geen algemeen letters')
else:
    print(letters)
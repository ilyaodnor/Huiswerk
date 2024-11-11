import random, os
with open('periode 3/week21/woorden.txt', 'r') as file:
    content = file.read()
worden = content.split()



def spel(worden):
    while True:
        ant = input('Wilt u spelen? (ja/nee) ').lower()
        
        if ant == 'ja':
            os.system('clear')
            #word = random.choice(worden)
            word = 'banaan' 
            word_letters = list(word)
            geheim_list = ['_' for _ in word_letters]  

            
            keeren = 10

            while keeren > 0: 
            
                
                print(f'Te raden woord: {"".join(geheim_list)}')
                print('-'*len(f'Je hebt nog {keeren} keren om het woord te raden!'))
                print(f'Je hebt nog {keeren} keren om het woord te raden!')
                print('')
                print('Veel succes')
                print('-'*len(f'Je hebt nog {keeren} keren om het woord te raden!'))
                letter = input('Voer letter in: ').lower() 
                
                if letter in geheim_list:
                    os.system('clear')
                    print('Je hebt deze letter al gehad, probeer een andere letter.')
                elif letter in word_letters:
                    for i in range(len(word_letters)):
                        if letter == word_letters[i]:
                            geheim_list[i] = letter
                    os.system('clear')
                    print('Dit is een goeie!')
                else:
                    os.system('clear')
                    print('Dit letter is niet in het woord, probeer opnieuw.')
                    keeren -= 1 
                
                if '_' not in geheim_list: 
                    os.system('clear')
                    print('Je hebt gewonnen!!')
                    print(f'Het woord was "{word}".')
                    break 
            else:  
                os.system('clear')
                print('Helaas, je hebt verloren.')
                print(f'Het woord was "{word}".')

        elif ant == 'nee':
            print('Bedankt voor het spelen!')
            break  
        else:
            print('Voer in "ja" of "nee"') 


spel(worden)  

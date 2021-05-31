import ast

def try_me():
    print("""
        Salut buddy !
        C'est mon premier package, soit indulgeant il ne contient pas grand chose !
        On se fait des petites additions ?
        A toi de jouer :)\n""")
    
    while True:     
        while True:
            try :
                add1 = ast.literal_eval(input('Entre le premier chiffre : '))
                add2 = ast.literal_eval(input('Entre le second chiffre : '))
                break
            except Exception as err:
                print("Petit malin, ce n'est pas un chiffre ! Réessaye : ")
        
        print(f'Le résultat de ton calcul {add1} + {add2} est égal à {add1 + add2}')
        print('Ctrl + c (ou Cmd + c) pour quitter !\n')
        print('On recommence !')
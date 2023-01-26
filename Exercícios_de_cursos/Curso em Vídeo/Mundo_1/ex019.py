"""
EX019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
"""
import random

def sorteio():
    a1=a2=a3=a4 = "Aluno"
    sort = random.randint(1, 4)
    if sort == 1:
        print(f'O aluno sorteado foi 1º{a1}')
    elif sort == 2:
        print(f'O aluno sorteado foi 2º{a2}')
    elif sort == 3:
        print(f'O aluno sorteado foi 3º{a3}')
    else:
        print(f'O aluno sorteado foi 4º{a4}')

    print(a1,a2,a3,a4)

sorteio()
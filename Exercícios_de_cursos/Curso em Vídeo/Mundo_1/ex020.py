"""
EX020 - Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
import random

def sorteio_aluno():
    a1 = str(input('Digite o Nome do primeiro aluno: '))
    a2 = str(input('Digite o Nome do segundo aluno: '))
    a3 = str(input('Digite o Nome do terceiro aluno: '))
    a4 = str(input('Digite o Nome do quarto aluno: '))
    lista = [a1, a2, a3, a4]
    sort = random.shuffle(lista)
    print(f'A lista ordenada entre os alunos é: ')
    print(lista)

sorteio_aluno()

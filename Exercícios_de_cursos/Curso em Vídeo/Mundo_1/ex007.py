"""
EX006 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

def media_aluno():
    n1 = int(input('Digite a primeira nota: '))
    n2 = int(input('Digite a segunda nota: '))
    med = (n1 + n2) / 2
    print(f'Sua primeira nota é {n1}\n'
          f'Sua segunda nota é {n2}\n'
          f'Sua média é {med}')

print(media_aluno())
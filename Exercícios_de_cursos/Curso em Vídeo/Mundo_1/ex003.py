"""
EX003 - Crie um programa que leia dois números e mostre a soma entre eles.
"""

def soma():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    soma = n1 + n2
    print(f'A soma de {n1} e {n2} é igual a {soma}')
print(soma())
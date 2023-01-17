"""
EX005 - Faça um programa que leia um número inteiro e moste na tela o seu
sucessor e seu antecessor.

"""

def antes_depois():
    n = int(input('Digite um número: '))
    antes = n - 1
    depois = n + 1
    print(f'Seu número é {n}, o antecessor é {antes} e o sucessor é {depois}')

print(antes_depois())
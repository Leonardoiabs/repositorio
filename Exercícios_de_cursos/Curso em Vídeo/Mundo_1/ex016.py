"""
EX016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex: Digite um número: 6.127
    O número 6.127 tem a parte inteira 6
"""

def parte_inteira():
    real = int(input('Digite um número real: '))
    porcao_inteira = real // 100
    print(f'A parte inteira de {real} é {porcao_inteira}')

parte_inteira()
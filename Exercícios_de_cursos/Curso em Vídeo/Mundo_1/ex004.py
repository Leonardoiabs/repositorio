"""
EX004 - Faça um programa que leia algo pelo
teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
"""

dado = input('Digite algum dado: ')
print(type(dado))
print(f'Seu dado é numérico?'.isnumeric())

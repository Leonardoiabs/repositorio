"""
EX011 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

Considere US$1,00 = R$3,27
"""

def converte_moeda():
    real = float(input('Digite a quantidade de reais que você possui: R$ '))
    dolar = real / 3.27
    print(f'Você possui em Dólares: US$ {dolar:.2f}')

print(converte_moeda())
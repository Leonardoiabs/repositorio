"""
EX002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
def boas_vindas():
    nome = input('Digite seu nome: ')
    print(f'Olá {nome}, Seja bem vindo!')

print(boas_vindas())
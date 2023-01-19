"""
EX015 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

def aumento_salarial():
    salario = float(input('Digite seu salário: R$ '))
    aumento = (salario / 100) * 15
    total = salario + aumento
    print(f'Seu salário atual é R$ {salario}\n'
          f'seu aumento foi de R$ {aumento}\n'
          f'SALÁRIO ATUAL R$ {total}')

aumento_salarial()
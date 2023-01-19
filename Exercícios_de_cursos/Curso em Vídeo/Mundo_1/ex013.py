"""
EX013 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

def desconto():
    preco = float(input('Digite o preço do produto: R$ '))
    desconto = (preco / 100) * 5
    total = preco - desconto
    print(f'O valor integral do produto é {preco}\n'
          f'Seu desconto foi de {desconto}\n'
          f'VALOR TOTAL: R$ {total}')

print(desconto())
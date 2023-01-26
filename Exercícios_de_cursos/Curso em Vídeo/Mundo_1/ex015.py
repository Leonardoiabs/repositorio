"""
EX015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
"""

def aluguel_de_carro():
    km_percorrido = int(input("Digite a quantidade de Km's rodados: "))
    dias = int(input('Digite a quantidade de dias que ficou com o veículo: '))
    km_valor = km_percorrido * 0.15
    valor_dia = dias * 60
    total_do_aluguel = km_valor + valor_dia
    print(f'O valor em quilometragem foi {km_valor}\n'
          f'O valor dos dias com o veículo é {valor_dia}\n'
          f'O TOTAL A PAGAR É: R$ {total_do_aluguel}')

aluguel_de_carro()
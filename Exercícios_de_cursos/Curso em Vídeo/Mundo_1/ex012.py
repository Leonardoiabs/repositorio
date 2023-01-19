"""
EX012 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m
"""

def pinta_parede():
    largura = float(input('Digite a largura da parede em metros: '))
    altura = float(input('Digite a altura da parede em metros: '))
    area = largura * altura
    tinta = area / 2
    print(f'A área da parede é {area} e você utilizará {tinta} latas de tinta para pintá-la!')

print(pinta_parede())
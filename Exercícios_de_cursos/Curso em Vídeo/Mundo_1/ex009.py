"""
EX009 - Escreava um programa que leia um valor em metros e mostre esse valor em centímetros e milímetros.

"""

def conversor():
    metro = float(input('Digite um número em metros: '))
    centimetro = metro / 100
    milimetro = metro / 1000
    print(f'O número digitado em metros é {metro}m, em centímetros é {centimetro}cm e em milímetros é {milimetro}mm.')

print(conversor())
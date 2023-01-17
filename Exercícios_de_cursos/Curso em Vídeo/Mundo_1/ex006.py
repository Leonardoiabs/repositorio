"""
EX006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""
from math import sqrt

def num():
    n = int(input('Digite um número: '))
    dobro = n * 2
    triplo = n * 3
    raiz = sqrt(n)
    print(f'O seu número é {n}, o dobro dele é {dobro}, triplo é {triplo} e a Raiz é {raiz}')

print(num())
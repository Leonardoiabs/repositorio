"""
EX010 - Crie uma Tabuada
"""

class tabuada:

    def soma():
        cont = 0
        print('-' * 10 + 'SOMA' + '-' * 10)
        while n > 0 and cont < 11:
            soma = n + cont
            print(f'{n} + {cont} = {soma}')
            cont += 1

    def subtracao():
        cont = 0
        print('-' * 10 + 'SUBTRAÇÃO' + '-' * 10)
        while n > 0 and cont < 11:
            sub = n - cont
            print(f'{n} - {cont} = {sub}')
            cont += 1

    def divisao():
        cont = 0
        print('-' * 10 + 'DIVISÃO' + '-' * 10)
        while n > 0 and cont < 11:
            div = n / cont
            print(f'{n} / {cont} = {div}')
            cont += 1

    def multiplicacao():
        cont = 0
        print('-' * 10 + 'MULTIPLICAÇÃO' + '-' * 10)
        while n > 0 and cont > 11:
            mult = n * cont
            print('{} * {} = {}'.format(n, cont, mult))
            cont += 1


print('=' * 10 + 'TABUADA' + '=' * 10)
n = int(input('Digite um número: '))
print(tabuada.soma())
print(tabuada.subtracao())
print(tabuada.divisao())
print(tabuada.multiplicacao())
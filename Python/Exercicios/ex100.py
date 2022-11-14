from random import randint
from time import sleep
def sorteia(lista):
    sleep(0.3)
    print('Sorteando 5 valores para a lista: ', end='')
    sleep(0.5)
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
        print('Pronto!')

def somaPar(lista):
    soma = 0
    for val in lista:
        if val % 2 == 0:
            soma = soma + val
    print(f'Somando os valores pares de {lista}, temos que a soma e: {soma}')

#Principal program
numeros = []
sorteia(numeros)
somaPar(numeros)
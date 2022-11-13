from random import randint
from  time import sleep
lista = []
jogos = []
print('-=-' * 30)
print('         JOGA NA MEGA SENA        ')
print('-=-' * 30)
qtd = int(input('Quantos jogos voce quer wue eu sorteie? '))
total = 1
while total <= qtd:
    i = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            i = i + 1
        if i >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1
print('-=-' * 3, f'SORTEANDO {qtd} JOGOS ', '-=-' * 3)
for p, v in enumerate(jogos):
    print(f'jogo {p + 1}: {v}')
    sleep(1)
print('-=-' * 5, '< BOA SORTE! >', '-=-' * 5)
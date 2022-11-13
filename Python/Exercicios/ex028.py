from random import randint
from time import sleep
computador = randint(0, 5) #radint gera um numero aleatorio e inteiro
print('-=-' * 30)
print('Computador: Irei pensar em um numero entre 0 e 5. Tente adivinhar... Isso se puder!')
print('-=-' * 30)
jogador = int(input('Jogador: Em que numero eu devo pensar? Digite um numero = '))
print('Processando a sua escolha...')
sleep(2)
if jogador == computador:
    print('Voce acertou, inacreditavel!')
    print('Voce escolheu = {} e o Computador gerou o numero = {}'.format(jogador, computador))
else:
    print('voce errou, infelizmente')
    print('Voce escolheu = {} e o Computador gerou o numero = {}'.format(jogador, computador))

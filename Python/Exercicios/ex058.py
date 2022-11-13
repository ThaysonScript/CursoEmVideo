from random import randint
computador = 0
palpites = 0
jogador = - 1
while jogador != computador:
    computador = randint(0, 10)
    jogador = int(input('Tente adivinhar o numero que o computador vai pensar: '))
    print('O computador pensou em:', computador)
    palpites = palpites + 1
print('Voce precisou de {} vezes para acertar o numero que o computador pensou.'.format(palpites))
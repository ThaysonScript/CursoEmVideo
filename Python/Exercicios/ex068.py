from random import randint
computador = randint(1, 2)
if computador == 1:
    computador = 'impar'
elif computador == 2:
    computador = 'par'
qtd = 0
while True:
    jogador = str(input()).lower().strip()
    if jogador == computador:
        print('Voce venceu')
        qtd = qtd + 1
    elif jogador != computador:
        print('voce perdeu')
        break
print('voce ganhou {} partidas consecutivas'.format(qtd))
from random import randint

computador = randint(1, 3)

if computador == 1:
    computador = 'pedra'
elif computador == 2:
    computador = 'papel'
elif computador == 3:
    computador = 'tesoura'

jogador = str(input())

if jogador == 'pedra' and computador == 'pedra':
    print('empate')

elif jogador == 'papel' and computador == 'papel':
    print('empate')

elif jogador == 'tesoura' and computador == 'tesoura':
    print('empate')

elif jogador == 'pedra' and computador == 'tesoura':
    print('ganhou')

elif jogador == 'tesoura' and computador == 'pedra':
    print('perdeu')

elif jogador == 'tesoura' and computador == 'papel':
    print('ganhou')

elif jogador == 'papel' and computador == 'tesoura':
    print('perdeu')

elif jogador == 'papel' and computador == 'pedra':
    print('ganhou')

elif jogador == 'pedra' and computador == 'papel':
    print('perdeu')

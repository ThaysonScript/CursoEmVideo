jogador = {}
partidas = []
jogador['Nome'] = str(input('Digite nome do jogador: '))
npartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for n in range(0, npartidas):
    partidas.append(int(input(f'    Quantos gols na partida {n}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print(jogador['Total'])
print('-=-' * 30)
print(jogador)
print('-=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for p, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {p}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')

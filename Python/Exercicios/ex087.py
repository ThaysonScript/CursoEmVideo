matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
SomaPar = maior = SomaColuna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite valor para [{l}, {c}] '))
print('-=-' * 30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            SomaPar = SomaPar + matriz[l][c]
    print()
print('-=-' * 30)
print(f'A soma dos valores pares e {SomaPar}')
for l in range(0, 3):
    SomaColuna = SomaColuna + matriz[l][2]
print(f'A soma dos valores da terceira coluna e {SomaColuna}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor valor da segunda linha e {maior}.')
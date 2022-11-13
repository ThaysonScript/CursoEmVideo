matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for Linha in range(0, 3):
    for Coluna in range(0, 3):
        matriz[Linha][Coluna] = int(input(f'Digite um valor para [{Linha}, {Coluna}]: '))
print('-=-' * 30)
for Linha in range(0, 3):
    for Coluna in range(0, 3):
        print(f'[{matriz[Linha][Coluna]}]', end='')
    print()
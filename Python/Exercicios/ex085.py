ListaNumero = [[], []]
vals = 0
for i in range(1, 8):
    vals = int(input(f'Digite valores para a posicao {i}: '))
    if vals % 2 == 0:
        ListaNumero[0].append(vals)
    elif vals % 2 == 1:
        ListaNumero[1].append(vals)
print('-=-' * 30)
ListaNumero[0].sort()
ListaNumero[1].sort()
print(f'Os valores pares digitados foram: {ListaNumero[0]}')
print(f'Os valores impares digitados foram: {ListaNumero[1]}')

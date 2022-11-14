ListaTemporaria = []
ListaDefinitiva = []
maior = menor = 0
while True:
    ListaTemporaria.append(str(input('Nome: ')))
    ListaTemporaria.append(float(input('Peso: ')))
    if len(ListaDefinitiva) == 0:
        maior = menor = ListaTemporaria[1]
    else:
        if ListaTemporaria[1] > maior:
            maior = ListaTemporaria[1]
        elif ListaTemporaria[1] < menor:
            menor = ListaTemporaria[1]
    ListaDefinitiva.append(ListaTemporaria[:])
    ListaTemporaria.clear()
    saida = str(input('Quer continuar? [S/N] '))
    if saida in 'Nn':
        break
print('-=-' * 30)
print(f'Ao todo, voce cadastrou {len(ListaDefinitiva)} pessoas.')
print(f'O maior peso foi de : {maior}kg. peso de ', end='')
for p in ListaDefinitiva:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
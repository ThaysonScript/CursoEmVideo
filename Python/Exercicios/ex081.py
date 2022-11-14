lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    saida = str(input('Quer continuar? [S/N] '))
    if saida in 'Nn':
        break
print('-=-' * 30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta na lista')

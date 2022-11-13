n = []
par = []
impar = []
while True:
    n.append(int(input('Digite um valor: ')))
    saida = str(input('Quer continuar? [S/N] '))
    if saida in 'Nn':
        break
for v in n:
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=-' * 30)
print(f'A lista completa e {n}')
print(f'A lista de pares e {par}')
print(f'A lista de impares e {impar}')
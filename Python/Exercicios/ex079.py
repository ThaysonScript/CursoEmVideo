lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor esta duplicado! Nao poderei adiciona-lo!')
    saida = str(input('Quer continuar: [S/N] '))
    if saida in 'Nn':
        break
print('-=-' * 30)
lista.sort()
print(f'Voce digitou os valores e organizei de forma crescente e ordenada: {lista}')

n = qtd = soma = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    qtd = qtd + 1
    soma = soma + n
print('Quantidade de numeros digitados foi = {}'.format(qtd))
print('A soma e = {}'.format(soma))
num = i = soma = 0
num = int(input())
while num != 999:
    soma = soma + num
    i = i + 1
    num = int(input())
print('voce digitou {} numeros e a soma entre eles foi {}.'.format(i, soma))

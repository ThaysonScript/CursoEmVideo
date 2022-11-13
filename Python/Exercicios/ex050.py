n1 = 0
for n in range(1, 7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        n1 = num + n1
        print(f'A soma dos pares e igual a = {n1}')
    else:
        print(f'O numero {num} nao e par')
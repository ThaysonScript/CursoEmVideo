n = int(input('Digite um numero para calcular o fatorial: '))
x = n
f = 1
print('Calculando o fatorial de {}! = '.format(n), end='')
while x > 0:
    print('{}'. format(x), end='')
    if x > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * x
    x = x - 1
print('{}'.format(f))

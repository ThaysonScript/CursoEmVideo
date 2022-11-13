n = 0
while n >= 0:
    n = int(input('Digite um numero para calcular sua tabuada da mult: '))
    if n < 0:
        break
    for x in range(1, 10):
        mult = n * x
        print('A tabuada do termo {} da mult do numero {} e igual a = {}'.format(x, n, mult))
print('Programa encerrado!')
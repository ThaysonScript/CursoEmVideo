num = int(input('Digite um numero: '))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(n), end=' ')
print('\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E primo')
else:
    print('Nao e primo')
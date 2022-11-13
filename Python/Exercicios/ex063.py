print('-'*30)
print('Sequencia')
print('-'*30)
n = int(input('Quantos termos? '))
t1 = 0
t2 = 1
print('='*30)
print('{} -> {}'.format(t1, t2), end='')
i = 3
while n >= i:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2  #1
    t2 = t3  #1
    i = i + 1
print(' -> Fim')

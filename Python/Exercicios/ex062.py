a1 = int(input())
r = int(input())
n = 1
total = 0
mais = 11
while mais != 0:
    total = total + mais
    while n != total:
        an = a1 + ((n - 1) * r)
        print('a p.a do termo {} e = {}'.format(n, an))
        n = n + 1
    mais = int(input('Quer mostrar mais termos? (para encerrar digite 0): '))
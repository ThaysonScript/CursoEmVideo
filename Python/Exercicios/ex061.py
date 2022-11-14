a1 = int(input())
r = int(input())
n = 1
while n != 11:
    an = a1 + ((n - 1) * r)
    print('a p.a do termo {} e = {}'.format(n, an))
    n = n + 1
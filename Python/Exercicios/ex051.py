#an = a1 + (n - 1) * r
a1 = int(input('Digite o primeiro termo da p.a: '))
r = int(input('Digite a razao da p.a: '))
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an)

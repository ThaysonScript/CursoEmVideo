from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1

    print('-=-' * 20)
    print(f'A contagem de {i} ate o {f} de {p} em {p} e: ', end=' ')
    sleep(2.5)

    n = i
    if i < f:
        while n <= f:
            print(n, end=' ')
            sleep(0.5)
            n = n + p
        print('FIM!')
        print()

    elif i >= f:
        n = i
        while n >= f:
            print(n, end=' ')
            sleep(0.5)
            n = n - p
        print('FIM!')
        print()


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=-' * 20)
print('Agora personalize sua contagem')
print()
ini = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
pas = int(input('Digite o passo: '))
contador(ini, fim, pas)
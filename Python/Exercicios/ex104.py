def leiaInt(msg):
    ok = False
    val = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            val = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
        if ok == True:
            break
    return val


# programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero: {n}')
print('''\nDigite valores para saber determinada tabuada do seu numero escolhido: \n
[ 1 ] Tabuada da soma
[ 2 ] Tabuada da subtracao
[ 3 ] Tabuada da multiplicacao
[ 4 ] Tabuada da divisao\n''')
numero = int(input('Digite um numero: '))
if numero == 1:
    soma = int(input('\nDigite um numero para a tabuada da soma: '))
    for n in range(0, 10):
        result = soma + n
        print('\no numero {} + {} e: {}'.format(soma, n, result))
elif numero == 2:
    subt = int(input('\nDigite um numero para a tabuada da subtracao: '))
    for n in range(0, 10):
        result = subt - n
        print('\no numero {} - {} e: {}'.format(subt, n, result))
elif numero == 3:
    mult = int(input('\nDigite um numero para a tabuada da multiplicacao: '))
    for n in range(0, 10):
        result = mult * n
        print('\no numero {} * {} e: {}'.format(mult, n, result))
elif numero == 4:
    div = int(input('\nDigite um numero para a tabuada da divisao: '))
    for n in range(0, 10):
        result = div / n
        print('\no numero {} * {} e: {}'.format(div, n, result))
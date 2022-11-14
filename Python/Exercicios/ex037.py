n = int(input('Digite um numero: '))
binario = str(input('Digite 1 para converter em Binario: '))
octal = str(input('Digite 2 para converter em Octal: '))
hexadecimal = str(input('Digite 3 para converter em Hexadecimal: '))
if binario == '1':
    bi = bin(n)
    print('Seu numero em binario e: ', bi[2::])
elif octal == '2':
    oc = oct(n)
    print('Seu numero em octal e: ', oc[2::])
elif hexadecimal == '3':
    hexa = hex(n)
    print('Seu numero em hexadecimal: ', hexa[2::])
else:
    print('Voce nao digitou nenhuma das escolhas de conversao acima')
print('Rode o programa novamente e escolha uma das opcoes para fazer a conversao.')
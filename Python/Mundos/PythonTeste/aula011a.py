'''stile:
0 = none
1 = bold
4 = underline
7 = negative
'''

'''
text:
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = roxo
36 = azul claro
37 = cinza
'''

'''
back:
40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = roxo
46 = azul claro
47 = cinza
'''

#Formato:
#\033[0;33;44m

'''
exemplos:
teste = print('\033[0;30;41mteste')
teste = print('\033[4;33;44mteste')
teste = print('\033[1;35;43mteste')
teste = print('\033[30;42mteste')
teste = print('\033[mteste')
teste = print('\033[7;30mteste')
'''

#exemplos de testes:
print('\033[1;31;43mHello World!\033[m')
print('\033[4;29;45mHello World!\033[m')
print('\033[7;29mHello World!\033[m')
print('\033[0;33;44mHello World!\033[m')
print('\033[7;33;44mHello World!\033[m')
a = 3
b = 5
print('Os valores sao \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a, b))
nome = 'Thayson'
print('Ola {}{}{}'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto_branco':'\033[7;30m'}
print('Ola {}{}{}'.format(cores['azul'], nome, cores['limpa']))

#dica, pesquisar colorise
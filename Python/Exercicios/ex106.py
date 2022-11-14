c = ['\033[m',          # 0 - sem cor
    '\033[0;30;41m',   # 1 - vermelho
    '\033[0;30;42m',   # 2 - verde
    '\033[0;30;43m',   # 3 - amarelo
    '\033[0;30;44m',   # 4 - azul
    '\033[0;30;45m',   # 5 - roxo
    '\033[7;30m'       # 6 - branco
    ]


def manual(msg):
    from time import  sleep
    sleep(0.5)
    print(c[5])
    print('''Bem vindo ao assistente para consultar comando do python:\n
             \n---------------------------Menu-------------------------
             \nDigite [1] para consultar o modulo que deseja.
             \nDigite ['Continuar'] para continuar com as consultas.
             \nDigite ['Fim'] para sair da consulta.
             \n--------------------------------------------------------''')
    print(c[5])
    cont = 0
    while True:
        print(c[1])
        if cont == 0:
            sleep(0.3)
            consult = str(input('Digite o modulo que deseja consultar pela primeira vez: '))
            print(f'O Modulo que voce procura e: {consult}\n')
            sleep(1)
            print(c[1])
            print(c[4])
            print(help(consult))
            cont = cont + 1
            print(c[4])
        if cont != 0:
            sleep(0.5)
            print(c[1])
            consult = str(input('Deseja continuar? ("continuar ou fim") ')).lower().strip()
            print(c[1])
            if consult in 'continuar':
                sleep(0.3)
                print(c[1])
                consult = str(input('Digite o modulo que deseja consultar novamente: '))
                print(f'O Modulo que voce procura e: {consult}\n')
                sleep(1)
                print(c[4])
                print(help(consult))
            if consult in 'fim':
                sleep(0.3)
                print(c[1])
                print('Estamos encerrando!')
                sleep(0.5)
                break
            else:
                print('Por favor! Digite apenas "continuar ou fim".')
                sleep(0.5)



# programa principal
print(c[1])
while True:
    usuario = str(input('Deseja realmete fazer a consulta?[S/N] '))
    if usuario in 'Ss':
        manual(usuario)
        break
    if usuario in 'Nn':
        print('\nFinalizando!')
        break
    else:
        print('Erro! Digite apenas [S/N]!')
    print(c[1])
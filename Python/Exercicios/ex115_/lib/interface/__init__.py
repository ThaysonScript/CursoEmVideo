def linha(tam=40):
    tamanho = tam * '-'
    return tamanho


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('Menu PRINCIPAL')
    count = 1
    for item in lista:
        print(f'{count} - {item}')
        count += 1
    print(linha())
    opc = leiaInt('Sua Opcao: ')
    return opc
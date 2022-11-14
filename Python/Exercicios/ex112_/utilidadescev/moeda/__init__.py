def aumentar(preco=0, taxa=0, formato=False):
    subiu = preco * (taxa/100)
    result = subiu + preco
    if formato is False:
        return result
    else:
        return moeda(result)


def diminuir(preco=0, taxa=0, formato=False):
    desceu = preco * (taxa/100)
    result = preco - desceu
    if formato is False:
        return result
    else:
        return moeda(result)


def metade(preco=0, formato=False):
    result = preco / 2
    if formato is False:
        return result
    else:
        return moeda(result)


def dobro(preco=0, formato=False):
    result = preco * 2
    if formato is False:
        return result
    else:
        return moeda(result)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaA=10, taxaR=5):
    print('-' * 35)
    print('RESUMO DO PREÇO'.center(30))
    print('-' * 35)
    print(f'O aumento de 10% foi de:\t{aumentar(preco, 10, True)}')
    print(f'Reduçao em 13% foi de: \t\t{diminuir(preco, 13, True)}')
    print(f'A metade e de: \t\t\t\t{metade(preco, True)}')
    print(f'O dobro e de: \t\t\t\t{dobro(preco, True)}')
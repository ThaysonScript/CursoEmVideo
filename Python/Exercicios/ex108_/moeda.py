def aumentar(preco=0, taxa=0):
    aumt = preco * (taxa/100)
    preco = aumt + preco
    return preco


def diminuir(preco=0, taxa=0):
    dim = preco * (taxa/100)
    preco = preco - dim
    return preco


def metade(preco=0):
    preco = preco / 2
    return preco


def dobro(preco=0):
    preco = preco * 2
    return preco


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

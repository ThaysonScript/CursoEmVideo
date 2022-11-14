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

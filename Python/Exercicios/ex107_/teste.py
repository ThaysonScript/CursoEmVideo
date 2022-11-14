def aumentar(n, taxa):
    aumt = n * (taxa/100)
    n = aumt + n
    return n


def diminuir(n, taxa):
    dim = n * (taxa/100)
    n = n - dim
    return n


def metade(n):
    n = n / 2
    return n


def dobro(n):
    n = n * 2
    return n

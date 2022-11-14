def fatorial(n, show=False):
    f = 1
    for v in range(n, 0, -1):
        if show == True and v > 1:
            print(f'{v} x ', end='')
        else:
            print(f'{v} = ', end='')
        f = f * v
    return f


# programa principal
print(fatorial(5, show=True))
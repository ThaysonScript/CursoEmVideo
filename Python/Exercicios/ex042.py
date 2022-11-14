retas = map(float, input().split())
r1, r2, r3 = retas
if r1 < r2 + r3:
    print('As retas formam um triangulo')
    if r1 == r2 == r3:
        print('O triangulo e equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
        print('O triangulo e isoceles')
    elif r1 != r2 != r3 != r1:
        print('O triangulo e escaleno')
else:
    print('As retas nao formam um triangulo')

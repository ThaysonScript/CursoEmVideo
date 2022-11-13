retas = map(float, input().split())
r1, r2, r3 = retas
if r1 < r2 + r3:
    print('As retas formam um triangulo')
else:
    print('As retas nao formam um triangulo')

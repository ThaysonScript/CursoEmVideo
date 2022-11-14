dist = float(input('qual e a distancia da sua viagem? '))
print('voce esta prestes a fazer uma viagem de {}km'.format(dist))
if dist <= 200:
    passag = dist * 0.50
    print('a distancia foi {} e sua passagem ficou de R$ = {}'.format(dist, passag))
else:
    passag = dist * 0.45
    print('a distancia foi {} e sua passagem ficou de R$ = {}'.format(dist, passag))

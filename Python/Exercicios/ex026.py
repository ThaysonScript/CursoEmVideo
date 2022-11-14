frase = str(input()).upper().strip()

print('quantidade de A que aparece e = {}'.format(frase.count('A')))

print('a primeira posicao que o A aparece e = {}'.format(frase.find('A') + 1))

print('a ultima posicao que o A aparece e = {}'.format(frase.rfind('A') + 1))

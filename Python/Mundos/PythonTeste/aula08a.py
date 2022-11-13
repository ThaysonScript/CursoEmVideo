import math #ou simplesmente escolhendo qual vai querer: from math import sqrt
num = int(input())
raiz = math.sqrt(num) #se for 'from math import sqrt' entao se tira o math.
print('A raiz do numero {} e igual a {:.3f}'.format(num, raiz))

#math.ceil() arredonda para cima
#math.floor() arredonda para baixo

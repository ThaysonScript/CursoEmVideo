import random
n1 = str(input())
n2 = str(input())
n3 = str(input())
n4 = str(input())
lista = [n1, n2, n3, n4]
random.shuffle(lista)
#shuffle e usado para embraralhar uma sequencia
print('A ordem de apresentacao sera = {}'.format(lista))
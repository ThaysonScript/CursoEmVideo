n1 = int(input())
n2 = int(input())

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
pot = n1 ** n2

#\n e para quebrar a linha
#end=' ' e para nao deixar quebrar a linha
print('A soma e {}, \n o produto e {} e a divisao e {:.3f}'.format(s, m, d), end=' ')
print('Divisao inteira {} e a potencia {}'.format(di, pot))
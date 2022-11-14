num = int(input())
n = str(num)
unid = n[3:4]
print(f'unidade = {unid}')
dez = n[2:3]
print(f'dezena = {dez}')
cent = n[1:2]
print(f'centena = {cent}')
milh = n[0:1]
print(f'milhar = {milh}')

'''
num = int(input())
u = num // 1 % 10
d = num // 10 % 10
c = num / 100 % 10
m = num // 1000 % 10
print('unidade e {}'.format(u))
print('dezena e {}'.format(d))
print('centena e {}'.format(c))
print('milhar e {}'.format(m))
'''
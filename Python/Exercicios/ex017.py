from math import sqrt
co = float(input())
ca = float(input())
ipt = sqrt((co ** 2) + (ca ** 2)) #ou simplesmente ' ** (1/2) ' para pegar a raiz
print(f'o co e {co}, o ca e {ca} e a ipt e {ipt:.2f}')

'''
ou 'import math' ou 'from math import hypot' dps se tira o math. se usar o from
entrada = co
entrada = ca
ipt = math.hypot(co, ca) isso calcula de uma vez
a hipotenusa de um triangulo retangulo
saida = print do ipt
'''

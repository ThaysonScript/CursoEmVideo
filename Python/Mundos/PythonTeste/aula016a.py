#tuplas sao imutaveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#fatiamento
print(lanche)
print(lanche[2])
print(lanche[-2])
print(lanche[-2:])
print(lanche[:-2])
print(lanche[0:4])
print(lanche[0:4:2])
print(lanche[:2])
print(lanche[2:])

#se colocar ' - ' ler a tupla do ultimo ate o inicio
print(lanche[-1])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi demais!')

#or

for n in range(0, len(lanche)):
    print(f'comendo de novo {lanche[n]} na posicao {n}')

#or

for pos, comida in enumerate(lanche):
    print(f'Eu vou mais uma vez comer {comida} na posicao {pos}')

print(sorted(lanche)) #coloca em ordem alfabetica
print(lanche)


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)

print(len(c)) #ler quantos elementos estao dentro da tupla
print(d.count(5)) #ler quantas vezes um numero aparece na tupla
print(b.index(8)) #ler em qual posicao esta o parametro passado pela primeira vez
print(d.index(5, 1)) #encontre em qual posicao o numero 5 esta a partir da posicao 1


pessoa = ('Thayson', 39, 'M', 99.88) #tupla aceita dados de qualquer valor
print(pessoa)
del(pessoa) # apaga uma variavel da memoria, so aceita apagando a tupla inteira
print(pessoa)
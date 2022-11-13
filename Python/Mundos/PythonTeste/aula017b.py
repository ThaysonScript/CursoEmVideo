#criando copias de listas, copia de dados
lista = []
listacopiada = []
lista.append(1)
lista.append(2)
lista.append(3)
listacopiada.append(lista[:])
print(listacopiada)

#criando ligacao entre listas
test = list()
test.append('Thayson')
test.append(40)
galera = list()
galera.append(test)
test[0] = 'Maria'
test[1] = 22
galera.append(test)
print(galera)

#criando copia de uma lista
test = list()
test.append('Thayson')
test.append(40)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)

#varias listas dentro de uma lista
galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['Maria', 45]]
print(galera[2][1])

#percorrendo a lista em um valor
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

#ou

galera = list()
dado = list()
totmai = totmen = 0
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade.')
        totmai = totmai + 1
    else:
        print(f'{p[0]} e menor de idade.')
        totmen = totmen + 1

print(f'temos {totmai} maiores e {totmen} menores de idade.')

#Entendendo a copia das listas:
'''
Se eu fizer duas listas, a primeira eu adiciono um valor e eu faco esse valor
ser recebido tambem na segunda lista. Fazendo isso eu terei uma ligacao entre as listas,
fazendo com que, caso eu troque o valor da primeira lista, o valor anterior da segunda lista
tambem sera substituido pelo valor atual adicionado da primeira lista, ficando assim, dois valores iguais
na segunda lista, o que foi substituido na primeira lista porque tem ligacao com a segunda lista e o que foi adicionado
que tambem e igual. Dessa forma, eu copio a primeira lista quando eu for adicionar na segunda lista, pois, assim,
eu nao terei ligacao e quando eu trocar o valor da primeira lista e for adicionar na segunda lista o valor que ja tava la
nao sera substituido.
EXEMPLO:
lista1 = []
lista2 = []
lista1.append('Thayson')
lista1.append(30)
lista2.append(lista1[:])
lista1[0] = 'abc'
lista1[1] = 15
lista2.append(lista1[:])
print(lista2)
Terminal::: lista2: [ ['Thayson', 30], ['abc', 15] ]
'''
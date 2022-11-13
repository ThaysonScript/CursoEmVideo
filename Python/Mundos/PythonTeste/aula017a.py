#lists #para criar lista pode ser "[]" ou " list()"
n = [2, 5, 9, 1]

#substituir valor em deteminada posicao
n[2] = 3

#adicionar valores
n.append(7)
print(n)

#ordenar do menor para o maior
n.sort()
print(n)

#ordenar do maior para o menor
n.sort(reverse=True)
print(n)

#saber o tamanho da lista, quantos elementos ela tem
print(f'Essa lista tem {len(n)} elementos.')

#adicionar valor em determinada posicao
n.insert(2, 2)
   #posicao  #valor
print(n)

#remover ultimo valor da lista
n.pop() #se adicionar um valor ao parametro ele entende como "remova o valor naquela posicao passada!"
print(n)

#remover a primeira vez que o valor aparece na lista
n.remove(2)
print(n)

#condicional para tentar tirar um valor que nao esta dentro da lista
if 4 in n:
    n.remove(4)
else:
    print('Nao achei o numero 4\n')

#percorrer valores acrescidos em uma lista
valors = []
valors.append(5)
valors.append(9)
valors.append(4)

for p, v in enumerate(valors):
    print(f'Na posicao {p} encontrei o valor {v}!')
print('cheguei ao fim da lista')

print('\n')

#pode ser tambem
valores = list()
for n in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

#criando uma ligacao entre listas
a = [2, 3, 4, 7]
b = a            #ligacao de lista
b = a[:] #cria uma copia da lista a
b[2] = 8         #em outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
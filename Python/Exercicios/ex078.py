lista = []
maior = menor = 0
for n in range(0, 5):
    lista.append(int(input(f'Digite numeros para a posicao {n}: ')))
    if n == 0:
        maior = menor = lista[n]
    elif lista[n] > maior:
        maior = lista[n]
    elif lista[n] < menor:
        menor = lista[n]
print(f'\nOs valores da lista sao: {lista}')
print(f'\nO maior numero da lista e: {maior}')
print(f'\nO menor numero da lista e: {menor}')
print('\n')
for p, v in enumerate(lista):
    print(f'O valor {v} esta na posicao {p}')
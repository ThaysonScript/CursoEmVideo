lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    #mostra produto
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='') # ' :.<30 ' alinhado a esquerda com 30 pontos
        #mostra preco
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)
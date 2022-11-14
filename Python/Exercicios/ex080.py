lista = [] #criando lista vazia
for i in range(0, 5): #lendo valores de 0 a 5
    num = int(input('Digite um valor: ')) #lendo valores do teclado
    if i == 0: # verificando se e a primeira posicao
        lista.append(num) #adicionando valor na lista na determinada posicao i
        print(f'foi adicionado na primeira posicao {num}')
    elif i > lista[-1]: #verifica se a posicao e maior que o ultimo valor na lista
        lista.append(num) #adiciona valor na lista
        print(f'foi adicionado na ultima posicao {num}')
    else:
        p = 0
        while p < len(lista): #enquanto o tamanho da lista for maior do que a posicao, execute!
            if num <= lista[p]: #verifica se o valor digitado for menor ou igual ao valor da lista na determinada posicao
                lista.insert(p, num) #insere valor em determinada posicao na lista
                print(f'foi adicionado na posicao {p} o valor {num}')
                break #sai do enquanto ( while )
            p = p + 1 # contador
print('-=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')

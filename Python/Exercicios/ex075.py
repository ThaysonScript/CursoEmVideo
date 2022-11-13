n = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
     int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {n.count(9)}')
if 3 in n:
     print(f'A primeira posicao em que apareceu o 3 foi:  {n.index(3)+1}')
else:
     print('O 3 nao foi digitado em nenhuma posicao!')
print('Os valores pares digitados foram: ', end='')
for x in n:
     if n % 2 == 0:
          print(n, end='')
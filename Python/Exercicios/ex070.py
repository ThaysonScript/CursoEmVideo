total = acima = menor = preço = n = 0
produto_barat = ''
print('Faça o cadastramento das suas compras!\n')
while True:
    produto = str(input('Digite o nome do produto: '))

    preço = float(input('Digite o preço do produto: '))
    while n != 1:
        menor = preço
        n = n + 1

    #total gasto na compra
    total = total + preço

    #produtos acima de 1000 real
    if preço > 1000:
        acima = acima + 1

    if preço <= menor:
        menor = preço
        produto_barat = produto
    continuar = str(input('Voce quer continuar a cadastrar suas compras? ')).upper().strip()[0]
    if continuar == 'N':
        break
print('O total gasto na compra foi de R$ {:.2f}'.format(total))
print('Os produtos que custaram mais de R$ 1000 foram: {}'.format(acima))
print('O produto mais barato foi [{}] e o seu preço foi de R$ {}'.format(produto_barat, menor))
val_casa = float(input('Digite o valor da casa: '))
sal_comprador = float(input('Digite o salario do comprador: '))
qtd_ano = int(input('Quantidade de anos para pagar: '))
meses = qtd_ano * 12
prestacao = val_casa / meses
minimo = sal_comprador * (30/100)
print('Para pagar uma casa de R$ {:.2f} em {} anos.'.format(val_casa, qtd_ano), end=' ')
print('A prestacao mensal sera de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser concedido!')
    print('Voce podera comprar esta casa')
else:
    print('Emprestimo sera negado!')
    print('Voce nao podera comprar esta casa')
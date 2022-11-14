#preço normal:
produto = float(input('Digite o preco do produto: '))

#condicoes de pagamento:
print('Meios de pagamento:')
print('dinheiro/cheque\na vista no cartao\n2x no cartao\n3x ou mais no cartao')
cond = str(input('Escolha o meio de pagamento: ')).upper().strip()

#ifs:
if cond == 'DINHEIRO' or cond == 'CHEQUE':
    desconto = produto * (10 / 100)
    precof = produto - desconto
    print('No dinheiro/cheque seu produto tera desconto de R$ {}\no preco final sera de R$ {}'.format(desconto, precof))

elif cond == 'CARTAO' or cond == 'A VISTA' or cond == 'A VISTA NO CARTAO' or cond == 'NO CARTAO':
    desconto = produto * (5 / 100)
    precof = produto - desconto
    print('A vista no cartao seu produto de R$ {} tera desconto de R$ {}'.format(produto, desconto))
    print('Valor final de R$ {}'.format(precof))

elif cond == '2X NO CARTAO' or cond == '2X':
    prod = produto
    print('Em 2x no cartao seu produto tera o mesmo preco de R$ ', prod)

elif cond == '3X OU MAIS NO CARTAO' or cond == '3X':
    juros = (produto * (20 / 100)) * parcelas
    preco_final = juros + produto
    print('sera acrescido R$ {} de juros ao seu produto de R$ {}'.format(juros, produto))
    print('Valor final de R$ {}'.format(preco_final))

km = float(input('Digite os km rodados: ')) #cada km e 0.15 real
dia_alugado = int(input('Digite os dias alugados: ')) #por dia 60 real
pag = (km * 0.15) + (dia_alugado * 60)
print('a quantidade de km rodado foi {}\nos dias alugados foram {}\nO pagamento total e {:.2f}'.format(km, dia_alugado, pag))

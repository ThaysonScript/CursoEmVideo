vel = float(input('Digite a velocidade atual do carro: '))
if vel > 80:
    print('voce foi multado')
    multa = (vel - 80) * 7
    print('voce tera que pagar de multa R$ = {:.2f}'.format(multa))
else:
    print('sua velocidade atual e = {} km/h'.format(vel))
    print('voce esta dentro da velocidade permitida')
print('\nTenha um bom dia e dirija com cuidado!')
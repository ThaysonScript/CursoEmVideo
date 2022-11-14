from datetime import date
atual = date.today().year
for n in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    nasc = atual - nasc
    falta = 21 - nasc
    if nasc < 21:
        print('Voce tem {} anos e para atingir a maioridade faltam {} anos'.format(nasc, falta))
    elif nasc >= 21:
        print('Voce tem {} anos e atingiu a maioridade'.format(nasc))
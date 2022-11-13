tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    user = int(input('Digite um numero entre 0 e 20: '))
    if user >= 0 and user <= 20:
        print(f'Voce digitou o numero {tupla[user]}')
        break
    else:
        print('Digite novamente, numero invalido!\n')
print('Fim de programa!')
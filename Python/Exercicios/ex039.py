from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos'.format(ano, idade))
if idade < 18:
    print('Voce ainda nao pode se alistar no serviço militar')
    tempo = 18 - idade
    print('Voce tem o prazo de {} anos ate o alistamento'.format(tempo))
elif idade == 18:
    print('Voce pode se alistar no serviço militar')
    tempo = 18 - idade
    print('Voce esta dentro do prazo atual de {} anos'.format(tempo))
elif idade > 18:
    print('Voce ja passou do prazo de alistamento do serviço militar')
    tempo = idade - 18
    print('Voce passou do prazo de {} anos'.format(tempo))

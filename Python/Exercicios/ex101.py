def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if 18 <= idade < 65:
        return f'Voce tem {idade} anos e o voto e obrigatorio!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Voce tem {idade} anos e o voto e opcional!'
    elif idade < 16:
        return f'Voce tem {idade} anos e o voto e negado!'


# Programa principal
nasc = int(input('Digite sua data de nascimento: '))
print(voto(nasc))
while True:
    saida = str(input('Quer continuar? [S/N] '))
    if saida in 'Nn':
        print('Fim de programa!')
        break
    elif saida not in 'Ss':
        print('Por favor digite somente [S/N]!')
    elif saida in 'Ss':
        nasc = int(input('Digite sua data de nascimento: '))
        print(voto(nasc))
pessoas = homens = mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('\nDigite o sexo: ')).strip().upper()[0]
    continuar = str(input('\nQuer continuar? ')).strip().upper()[0]
    if idade >= 18:
        pessoas = pessoas + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulher = mulher + 1
    if continuar == 'N':
        break

print('\nQuantidade de pessoas maiores de 18 anos: {}'.format(pessoas))
print('Quantidade de homens cadastrados: {}'.format(homens))
print('Quantidade de mulheres menores de 20 anos: {}'.format(mulher))
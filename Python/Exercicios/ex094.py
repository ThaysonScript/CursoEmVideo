galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['Sexo'] = str(input('Digite o sexo: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('Invalido. Digite apenas [M/F].')
    pessoa['Idade'] = int(input('Digite a idade: '))
    soma = soma + pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        saida = str(input('Quer continuar? [S/N] ')).upper()[0]
        if saida in 'SN':
            break
        else:
            print('Invalido. Digite apenas [S/N].')
    if saida == 'N':
        break
print('-=-' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade e de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('D) Lista das pessoas que estao acima da media: ')
for p in galera:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< FINALIZANDO >>')

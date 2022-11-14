from  datetime import datetime
dicionario = {}
dicionario['Nome'] = str(input('Digite nome: '))
nascimento = int(input('ano de nascimento: '))
dicionario['Idade'] = datetime.now().year - nascimento
dicionario['CTPS'] = int(input('Carteira de Trabalho: '))
if dicionario['CTPS'] != 0:
    dicionario['Contratacao'] = int(input('Ano de Contratacao: '))
    dicionario['Salario'] = float(input('Salario: R$'))
    dicionario['Aposentadoria'] = dicionario['Idade'] + ((dicionario['Contratacao'] + 35) - datetime.now().year)
print('-=-' * 30)
for k, v in dicionario.items():
    print(f'  - {k} tem o valor {v}')

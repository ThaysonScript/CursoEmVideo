#criar um dicionario
pessoas = {'nome': 'Thayson', 'sexo': 'M', 'idade': 22}

#imprimir um dicionario
print(pessoas)
print(f'O nome e {pessoas["nome"]} a idade e {pessoas["idade"]} e o sexo e {pessoas["sexo"]}')

#mostrar chaves
print(pessoas.keys())

#mostrar valores
print(pessoas.values())

#mostrar todos os items do dicionario
print(pessoas.items())

#mostrar por meio de lacos
for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

#deletar uma coisa dentro do dicionario
del pessoas['sexo']

#adicionar uma coisa dentro do dicionario
pessoas['peso'] = 90.5
print(pessoas)

#criar dicionario dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

#copiar dicionarios
estado = dict()
brasil = list()
for i in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.') # ou for v in e.values() >>>> print(v)
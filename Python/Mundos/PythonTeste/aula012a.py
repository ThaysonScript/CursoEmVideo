#estrutura condicional aninhada
nome = str(input('Qual e o seu nome? ')).upper()
if nome == 'THAYSON':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome e bem popular no Brasil.')
elif nome in 'ANA CLAUDIA JESSICA JULIANA':
    print('Belo nome feminino!')
else:
    print('Seu nome e bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

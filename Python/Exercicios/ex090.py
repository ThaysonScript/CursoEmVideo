aluno = {}
aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input('media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'
print('-=-' * 30)
for k, v in aluno.items():
    print(f'- |{k} e igual a {v}')

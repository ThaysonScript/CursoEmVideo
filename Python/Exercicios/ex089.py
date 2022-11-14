alunos = []
n = 0
while True:
    al= str(input('Digite o nome do aluno: '))
    nt1 = int(input('Digite nota 1: '))
    nt2 =  int(input('Digitw nota 2: '))
    media = (nt1 + nt2) / 2
    alunos.append([al, [nt1, nt2], media])
    saida = str(input('Quer continuar? Digite qualquer coisa e para parar digite: [N/n] '))
    if saida in 'Nn':
        break
while n != len(alunos):
    print(f'\nO aluno {alunos[n][0]} ficou com media: {alunos[n][2]}')
    n = n + 1
while True:
    ver = str(input('\nDeseja ver notas individuais? '))
    if ver in 'Nn':
        break
    if ver in 'Ss':
        qual = int(input('\nDeseja ver a de qual aluno? Digite a sua posicao: '))
        if qual <= len(alunos) - 1:
            print(f'\nO aluno {alunos[qual][0]} tirou as notas: {alunos[qual][1]}')
        else:
            print('\nAluno invalido! Digite a posicao do aluno na lista.')
    else:
        print('\nFavor, digitar [S/N]!')
print('\nVoce finalizou o programa!')
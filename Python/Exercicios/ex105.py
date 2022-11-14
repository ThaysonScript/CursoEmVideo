def notas(*n, sit=False):
    '''
    ---> Funcao que analisa notas e situacoes de varios alunos
    :param n: uma ou mais notas de alunos
    :param sit: valor opcional que indica a situacao das notas
    :return: retorna um dicionario com informacoes sobre a situacao das notas dos alunos.
    '''
    result = {}
    result['Total'] = len(n)
    result['Maior'] = max(n)
    result['Menor'] = min(n)
    result['Media'] = sum(n) / len(n)
    if sit == True:
        if result['Media'] >= 7:
            result['Situacao'] = 'Boa'
        elif result['Media'] >= 5:
            result['Situacao'] = 'Razoavel'
        else:
            result['Situacao'] = 'Ruim'
    return result


# programa principal
nts = notas(5.5, 2.5, 1.5, sit=True)
print(nts)
help(notas)
from ex115_.lib.interface import *
from ex115_.lib.arquivo import *
from time import sleep

arq = 'CursoEmVideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        # Ver pessoas cadastras
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastra novas pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Digite um novo nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair do programa
        cabecalho('SAINDO DO PROGRAMA...')
        break
    else:
        # Digitou opcao errada no menu.
        print('ERRO! Digite uma opcao valida!')
    sleep(2)

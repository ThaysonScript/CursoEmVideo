#interact help:

#help(#alguma funcao do python como print)
help(print)

#pode ser tambem: __doc__
print(print.__doc__)

# --------------------------------------------

#ou pode colocar no python console o help() e ele ja muda para o "ajuda interativa"
#e coloque o modulo que deseja consultar
#Digite "quit" para retornar para o terminal do python

# -----------------------------------------------------------------------------------------

#Docstrings: Documentacao de strings
#ler uma string dentro de algum modulo criado

def contador(i, f, p):
    '''
    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c = c + p
    print('Fim!')

help(contador)

# ------------------------------------------------------------------------------------------

#parametros opcionais:
#caso eu nao passe um parametro eu posso atribuir um valor interno a ele
#ex: se c for invalida, ou seja, nao for passado valor nenhum... atribua valor 0 a ele.

def soma(a=0, b=0, c=0):
    '''
    --> Faz a soma de 3 valores e mostra na tela.
    :param a: 1 valor
    :param b: 2 valor
    :param c: 3 valor
    :return: nada
    '''
    s = a + b + c
    print(f'A soma e: {s}')


soma()

# ---------------------------------------------------------------------------------------------
'''
#Escopo de Variaveis:

def teste():
    #Escopo local, variaveis locais, somente acesso se for local
    #pode-se criar "global n" para pegar o valor global e atribuir o seu valor dentro do escopo local sem criar um novo espaco em memoria
    x = 8
    print(f'Na funcao teste, n vale {n}')
    print(f'Na funcao teste, x vale {x}')


#programa principal
#escopo global, variaveis globais, acesso em todos os lugares, pois e uma estrutura global
n = 2
print(f'No programa principal, n  vale {n}')
teste()
print(f'No programa principal, x  vale {x}')
'''
# ---------------------------------------------------------------------------------------------------------------------------------------------

#Retornando valores:

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s #retorna a variavel que ta sendo usada


#programa principal
     # s = a + b + c
r1 = soma(3, 2, 5) # A variavel que foi retornada pode ser usada como valor de outra variavel
r2 = soma(1, 7)
r3 = soma(4)
print(f'Meus calculos deram {r1}, {r2} e {r3}.')
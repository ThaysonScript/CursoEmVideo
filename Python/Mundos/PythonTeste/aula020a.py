'''
print('-' * 30)
print('   CURSO EM VIDEO   ')
print('-' * 30)
print('-' * 30)
print('   APRENDA PYTHON   ')
print('-' * 30)
print('-' * 30)
print('   THAYSON GUEDES   ')
print('-' * 30)
'''

#===========================================================

def lin():
    print('-' * 30)


#programa principal
lin()
print('   CURSO EM VIDEO   ')
lin()
print('   APRENDA PYTHON   ')
lin()
print('   THAYSON GUEDES   ')
lin()

#=========================================================

def menssagem(msg):
    lin()
    print(msg)
    lin()


#Programa Principal
menssagem('SISTEMA DE ALUNOS')

#=============================================================

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


#Programa principal
titulo('   CURSO EM VIDEO   ')
titulo('   APRENDA PYTHON   ')
titulo('   THAYSON GUEDES   ')

#========================================================

'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
'''

     #parametros
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa Principal
soma(4, 5)    #sempre tera que passar a mesma quantidade de parametros que foi definido na funcao
soma(a=8, b=9)    #pode explicitar qual e o parametro
soma(b=2, a=1)

#====================================================================================================

#empacotamento
def contador(* num): #   * num vai ler varios valores aos quais nao tem certeza de quantos sao.
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


#Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#OU

'''
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')
    
Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

#==============================================================================================

def dobra(lista):
    posicao = 0
    while posicao <= len(lista):
        lista[posicao] = lista[posicao] * 2
        posicao = posicao + 1


#Programa Principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#=======================================================

#desempacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando os valores {valores} temos {s}')


#Programa Principal
soma(5, 2)
soma(2, 9, 4)
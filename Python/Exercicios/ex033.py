#recebendo valores do teclado
n1 = float(input())
n2 = float(input())
n3 = float(input())
#atribuindo valor maior e menor
maior = n1
menor = n3
#testando a condicao maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('maior: ',maior)
#testando a condicao menor
if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
print('menor: ',menor)

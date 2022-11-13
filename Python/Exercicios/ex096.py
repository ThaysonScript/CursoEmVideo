def area(largura, comprimento):
    a = largura * comprimento
    print(f'A largura {largura} e o comprimento {comprimento} e de {a}m^2.')


#Programa Principal
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
area(largura, comprimento)
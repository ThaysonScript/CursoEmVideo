def escreva(txt):
    p = 0
    while p < len(txt):
        print('~', end='')
        p = p + 1


#Programa Principal
texto = str(input('Digite um texto: '))
escreva(texto)
print()
print(texto)
escreva(texto)

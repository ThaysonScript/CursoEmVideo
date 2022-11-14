from ex107_ import teste

# Programa Principal
num = float(input('Digite um numero: '))
print(f'O aumento de 10% do numero {num} foi de: {teste.aumentar(num, 10)}')
print(f'Reduzindo o numero {num} em 13%, temos que foi de: {teste.diminuir(num, 13)}')
print(f'A metade do numero {num} e de: {teste.metade(num)}')
print(f'O dobro do numero {num} e de: {teste.dobro(num)}')

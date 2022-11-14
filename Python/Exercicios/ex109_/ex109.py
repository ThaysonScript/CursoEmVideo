from ex109_ import moeda

# Programa Principal
num = float(input('Digite um numero: '))
print(f'O aumento de 10% do numero {moeda.moeda(num)} foi de: {moeda.aumentar(num, 10, True)}')
print(f'Reduzindo o numero {moeda.moeda(num)} em 13%, temos que foi de: {moeda.diminuir(num, 13, True)}')
print(f'A metade do numero {moeda.moeda(num)} e de: {moeda.metade(num, True)}')
print(f'O dobro do numero {moeda.moeda(num)} e de: {moeda.dobro(num, True)}')

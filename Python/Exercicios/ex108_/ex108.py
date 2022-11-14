from ex108_ import moeda

# Programa Principal
num = float(input('Digite um numero: '))
print(f'O aumento de 10% do numero {moeda.moeda(num)} foi de: {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Reduzindo o numero {moeda.moeda(num)} em 13%, temos que foi de: {moeda.moeda(moeda.diminuir(num, 13))}')
print(f'A metade do numero {moeda.moeda(num)} e de: {moeda.moeda(moeda.metade(num))}')
print(f'O dobro do numero {moeda.moeda(num)} e de: {moeda.moeda(moeda.dobro(num))}')

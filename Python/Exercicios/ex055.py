maior_peso = 0
menor_peso = 0
for n in range(1, 6):
    peso = float(input('Digite o peso de 5 pessoas, {} de 5: '.format(n)))

    if peso > maior_peso:
        maior_peso = peso
        menor_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print(f'O maior peso e {maior_peso}')
print(f'O menor peso e {menor_peso}')

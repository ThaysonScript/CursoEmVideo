def maior(* num):
    i = maior = 0
    for valor in num:
        print(f'{valor} ', end='')
        if i == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        i = i + 1
    print(f'Os valores informados foram: {i} ao todo')
    print(f'O maior valor informado foi: {maior}')


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
menu = 0
nv_n1 = 0
nv_n2 = 0
while menu != 5:
    print('''[1] Somar? 
    [2] Multiplicar? 
    [3] Maior? 
    [4] Novos valores? 
    [5] Sair do programa? ''')
    menu = int(input('\nQual a sua escolha? '))
    if menu == 1:
        valor1 = int(input('Digite o valor 1: '))
        valor2 = int(input('Digite o valor 2: '))
        soma = valor1 + valor2
        print('A soma dos seus valores e: {}'.format(soma))
    elif menu == 2:
        valor1 = int(input('Digite o valor 1: '))
        valor2 = int(input('Digite o valor 2: '))
        mult = valor1 * valor2
        print('A multiplicacao dos seus valores e: {}'.format(mult))
    elif menu == 3:
        valor1 = int(input('Digite o valor 1: '))
        valor2 = int(input('Digite o valor 2: '))
        if valor1 > valor2:
            print('Valor maior e: ',valor1)
        elif valor1 == valor2:
            print('Nenhum valor e maior. Todos sao iguais!')
        else:
            print('Valor maior e: ',valor2)
    elif menu == 4:
        nv_n1 = int(input('\nO numero que sera digitado e o seu novo primeiro numero: '))
        nv_n2 = int(input('\nO numero que sera digitado e o seu novo segundo numero: '))
        print('\nOs valores que voce armazenou foram: {} para o primeiro e {} para o segundo valor.\n'.format(nv_n1, nv_n2))
    elif menu == 5:
        menu = int(input('Quer realmente sair do programa? (Digite novamente 5): '))

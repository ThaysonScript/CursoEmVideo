#1671
n50 = n20 = n10 = n1 = 0
while True:
    sacar = int(input('Digite o valor que quer sacar: '))
    n50 = sacar // 50 #33
    n20 = (sacar - (n50 * 50)) // 20
    n10 = (sacar - ((n50 * 50) + (n20 * 20))) // 10
    n1 = (sacar - ((n50 * 50) + (n20 * 20) + (n10 * 10))) // 1

    print('''O saque foi feito com sucesso!\n
    Aqui esta dividido o seu saque em cedulas disponiveis:\n
    Cedulas de [50]: {}\n
    Cedulas de [20]: {}\n
    Cedulas de [10]: {}\n
    Cedulas de [1]: {}'''.format(n50, n20, n10, n1))
    continuar = str(input('Deseja continuar o saque? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Saque finalizado totalmente!')

s = 0 #somador
for n in range(1, 501): #laço
    if n % 2 == 1: #valores impares
        if n % 3 == 0: #valores impares que sao multiplos de 3
            s = s + n
            print(s)
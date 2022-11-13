r = 'S'
soma = qtd = media = maior = menor = 0
while r in 'sS':
    num = int(input('Digite um numero: '))
    soma = soma + num
    qtd = qtd + 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / qtd
print('Voce digitou {} numeros e a media foi {}'.format(qtd, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))

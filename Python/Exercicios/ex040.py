notas = map(float, input('Digite na mesma linha as suas duas notas: ').split())
n1, n2 = notas
media = (n1 + n2) / 2
if media < 5:
    print('Voce esta reprovado')
elif media >= 5 and media <= 6.9:
    print('Voce esta em recuperacao')
elif media >= 7:
    print('Voce esta aprovado')

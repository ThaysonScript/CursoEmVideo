vals = map(float, input().split())
peso, altura = vals
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
    print('Seu peso e: {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
    print('Seu peso e: {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
    print('Seu peso e: {:.2f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade')
    print('Seu peso e: {:.2f}'.format(imc))
elif imc >= 40:
    print('Obesidade morbida')
    print('Seu peso e: {:.2f}'.format(imc))

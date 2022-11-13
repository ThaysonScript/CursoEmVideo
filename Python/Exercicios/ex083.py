expr = str(input('Digite uma expressao: '))
pilha = []
for n in expr:
    if n == '(':
        pilha.append('(')
    elif n == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao e valida!')
else:
    print('Sua expressao e invalida!')
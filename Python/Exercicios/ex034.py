sal = float(input())
if sal <= 1.250:
    aumento = (sal * (15 / 100)) + sal
    print('salario antes {:.3f} e depois do aumento: {:.3f}'.format(sal, aumento))

if sal > 1.250:
    aumento = (sal * (10 / 100)) + sal
    print('salario antes {:.3f} e depois do aumento: {:.3f}'.format(sal, aumento))

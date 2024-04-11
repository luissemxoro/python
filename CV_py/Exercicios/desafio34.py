sal = float(input('Digite o salario do funcionario: '))
lim = float(1250.00)

if sal > lim:
    div = (10/100)*sal
    vlr = sal+div
    print('O seu novo salario é {}'.format(vlr))

else:
    div2 = (15/100)*sal
    vlr2 = sal+div2
    print('O novo salario é {}'.format(vlr2))
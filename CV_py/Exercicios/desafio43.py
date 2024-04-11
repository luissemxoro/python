p = float(input('Digite o seu peso em KG: '))
a = float(input('Digite a sua altura em M: '))

m1 = (p/a) / a
print('{:.2f}'.format(m1))
if m1 < 18.5:
    print('Abaixo do peso!')
elif m1 >= 18.5 and m1 < 25:
    print('Peso ideal!')
elif m1 >= 25 and m1 < 30:
    print('Sobrepeso!')
elif m1 >= 30 and m1 <= 40:
    print('Obesidade!')
elif m1 > 40: 
    print('\033[31mObesidade Morbida\033[m')


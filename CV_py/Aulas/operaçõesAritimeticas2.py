n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
print('')

print('A soma vale {}, o produto é {} e a divisão {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

print(f'A soma vale {s}, \n o produto vale {m} e a divisão vale {d:.2f}')
print(f'Divisão inteira {s}, o produto vale {m} e a divisão')

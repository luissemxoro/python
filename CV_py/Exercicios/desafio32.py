n = int(input('Digite um ano qualquer: '))

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano é BIXESTO!')
else:
    print('O ano não é BIXESTO!')
n = int(input('Digite um numero inteiro: '))
o = int(input('Digite a conversão que você quer:\n [1] para binário\n [2] para octal\n [3] para hexadecimal:\n '))

if o == 1:
    print(bin(n))
elif 0 == 2: 
    print(oct(n))
else:
    print(hex(n))
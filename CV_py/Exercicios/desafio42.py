r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta:'))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Pode Gerar um triangulo!')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('É um triangulo EQUILATERO')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:
        print('É um triangulo ISOCELES')
    else:
        print('É um triangulo ESCALENO')
    
    
else:
    print('NÃO PODE GERAR um triângulo!!!')
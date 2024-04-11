vel =  float(input('Digite a velocidade em Km/h: '))

if vel > 80 :
    
    mul = (vel-80) * 7.00
    print(f'Você foi multado! Você passou a {vel}Km/h, a multa é de valor R${mul}.')

else:
    print('Parabéns!!! Você está dentro da velocidade limite da pista')
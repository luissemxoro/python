dist = float(input('Digite a distância da viagem em Km: '))

vlr1 = dist * 0.50
if dist <= 200:
  
    print(f'A distância da viagem é {dist} e o valor ficará R${vlr1:.2f}')

else:
    vlr2 = dist * 0.45
    print(f'A distância é {dist}, está acima de 200Km. O valor ficará R${vlr2:.2f}')
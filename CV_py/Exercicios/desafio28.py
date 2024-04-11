import random 
num = random.randint(1,5)
pess = int(input("Digite o numero que você acha que foi sorteado: "))

if num == pess:
    print(f'Você acertou! o numero é: {num}')
else:
    print(f'Você errou, o numero sorteado foi {num}')
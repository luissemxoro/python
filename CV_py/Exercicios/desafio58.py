import random
tentativas = 0
dig = 0
num = random.randint(0,10)
while dig != num:
    dig = int(input("Tente acertar o numero de 1 a 10 que eu estou pensando: "))
    tentativas += 1
print("Parabens!!!Você acertou!!!\nDepois de {} tentativas".format(tentativas))
num = 0
for c in range(1,7):
    num2 = int(input("Digite um numero: "))
    if num2 % 2 == 0:
        num = num + num2
        print("A soma está em {}".format(num))
    else:
        print("A soma esta em {}".format(num))

print("A soma dos numeros deu {}".format(num))
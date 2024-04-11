# Desafio 52
num = int(input("Digite um número: "))
if num > 1:
    primo = True
    for c in range(2, num):
        if num % c == 0:
            primo = False
            break

    if primo:
        print("{} é um número primo!!!".format(num))
    else:
        print("{} não é um número primo!".format(num))
else:
    print("{} não é um número primo!".format(num))
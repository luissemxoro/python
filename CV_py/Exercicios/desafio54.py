from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (1,7):
    d = int(input("Digite um ano de nascimento: "))
    s = atual - d
    if s >= 21:
        print("É de maior!")
        maior = maior + 1
    else:
        print("É de menor!")
        menor = menor + 1

print("\033[33m{}\033[m pessoas são de \033[32mMAIOR\033[m e \033[33m{}\033[m pessoas são de \033[31mMENOR\033[m".format(maior, menor))
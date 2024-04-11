escolha = 0
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))


while (escolha != 5 ):
    
    escolha = int(input("Escolha uma das opções: \n[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos Números \n[5]Sair do programa\n"))
   

    if escolha == 1:
        print("A soma de {} + {} é \033[32m{}\033[m.".format(num1, num2, num1 + num2))
        print("="*20)
    elif escolha == 2:
        print("A multiplicação entre {} e {} é \033[31m{}\033[m.".format(num1, num2, num1*num2))
        print("="*20)
    elif escolha == 3:
        if num1 > num2:
            print("Entre {} e {} o maior numero é \033[31m{}\033[m".format(num1, num2, num1))
            print("="*20)
        elif num2 > num1:
            print("entre {} e {} o maior numero é \033[31m{}\033[m".format(num1, num2, num2))
            print("="*20)
        else:
            print("Os numeros são iguais")
            print("="*20)
    elif escolha == 4:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
        print("="*20)
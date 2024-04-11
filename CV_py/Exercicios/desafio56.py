idade = 0
mais_velho = 0
contador_mulheres = 0
nome_mv = ''
sexo1 = ''
for pessoas in range (1,3):
    print("---- {}ª Pessoa -----".format(pessoas))
    nome = input("Nome: ")
    idade_digitada = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    idade = idade + idade_digitada

    if pessoas == 1:
        sexo1 = "A mulher mais velha"
        nome_mv = nome
    
    if idade_digitada > mais_velho:
        mais_velho = idade_digitada
        nome_mv = nome
        if sexo == "F":
            sexo1 = "A mulher mais velha"
           
        else:
            sexo1 == "O homem mais velho "
           
    if sexo == "F" and idade_digitada < 21:
        contador_mulheres = contador_mulheres + 1

media_idade = idade / 4
print("A média de idade é: {}".format(media_idade))
print("{} tem {} anos e se chama {}".format(sexo1, mais_velho, nome_mv))
print("Tem {} mulheres menores de 21 anos de idade!".format(contador_mulheres))
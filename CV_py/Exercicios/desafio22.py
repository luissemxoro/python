nome = input('Digite seu nome: ')
print(f'Seu nome é: {nome}')


print('seu nome em maiusculo é: ' +nome.upper())
print('Seu nome em minusculo é: ' +nome.lower())

dividindo = nome.split()

cont = len(nome.strip())
print(f'Tem {cont} indices')

es = nome.count(' ')
print(f'Você digitou {es} espaços')

frase = nome.replace(' ','') #Tira espaços e sobe pra memoria a alteração
n = len(frase) 
print(f'O seu nome tem {n} letras')

dv1 = len(dividindo[0])
print(f'O primeiro nome tem {dv1} letras')

# PARA ENTENDER MELHOR VOLTAR NA AULA DE MANIPULANDO TEXTOS

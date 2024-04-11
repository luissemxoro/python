import random 

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ') 
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

j = [n1, n2, n3, n4]

random.shuffle(j)
print(f'A ordem de apresentação é:\n\n1º: {j[0]}\n2º: {j[1]}\n3º: {j[2]}\n4º: {j[3]}')

# O .shuffle Embaralha a lista ex.: Linha 10
# A parte  {j[0]} funciona assim:
# O 'j' chama a lista que foi embarlhada na linha 10.
# O [0] mostra a posição onde cada elemento vai entrar.
#



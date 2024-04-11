#MODO COM REPETIÇÕES


frase = input("Digite uma frase:  ").upper().strip()
print(frase)
frase = frase.split()
print(frase)
frase = ''.join(frase)
print(frase)
i = ''
for l in range(len(frase) -1, -1, -1):
  i += frase[l]
if i == frase:
  print("A frase \033[31m{}\033[m, de traz pra frente fica \033[32m{}\033[m, então ela é um palíndromo!!!".format(i,frase))
else:
  print("A frase {} não é um palindromo".format(frase))
  

					#***BY LUIS***
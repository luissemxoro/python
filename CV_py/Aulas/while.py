#for c in range (1,10):
#   print(c)
# print('Fim')

#c = 1
#while c < 11:
#    print(c)
#    c = c + 1
#print("fim")

n =1 
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} numeros pares e {} numeros impares".format(par, impar))
print("Acabou")
t1 = float(input("Digite o termo: "))
p = float(input("Digite o valor da proguessão: "))

for c in range (1,11):

    t1 = t1 + p 
    
    print(t1)
print("="*25)

#Mesma coisa mas modos diferentes de fazer
t = 0
t = float(input("Digite um termo: "))
p2 = float(input("Digite um progressao: "))
print('-'*15)
print(t)
for c in range (1,10):
    t = t + p2
    print(t)
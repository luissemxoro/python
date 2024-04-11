maior = 0
menor = 0

for c in range (1,6):
    p = float(input("Qual é o peso da {}ª pessoa: ".format(c)))
    if c == 1:
         maior = p
         menor = p 
    else:
         if p > maior:
            maior = p
         if p < menor:
            menor = p
    print("O maior {}, O menor {}".format(maior,menor))
    if c == 5:
        print("\n")
print("="*25)
print("\n")

print("O maior peso descrito foi de {}Kg".format(maior))
print("O menor peso descrito foi {}Kg".format(menor))
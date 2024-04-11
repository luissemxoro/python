from math import pow, sqrt
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
co2 = pow(co,2) 
ca2 = pow(ca,2)

hi = co2 + ca2

print ('O valor do Cateto Oposto é {}, o valor do Cateto Adjacente é {}.\nEntão o valor da Hipotenusa é {}'.format (co, ca, sqrt(hi)))
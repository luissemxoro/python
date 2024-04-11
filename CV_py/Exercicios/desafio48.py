a = 0
b = 0
for c in range (1,501,2):
    if c % 3 == 0:
       a = a + c
       #A letra a serve como uma variavel de soma, ela começa com 0 e vai somando cada numero impar divisivel por 3 que o resultado é 0, e toda vez que der certo, vai somar esse numero com os proximos que derem certo.
       b = b + 1 
       #A letra B serve como contador, cada vez q achar um numero impar divisivel por 3 que dá 0, acrescentará mais um numero na contagem, assim contando a quantidade de numeros que deram certo na condição.
print("A soma de todos os numeros impares, divisiveis por 3, que se resulta em 0 é {}, foi a quantidade de {} numeros somados".format(a,b))


frase = 'Curso em Video Python'
print(frase)

#O indice é começado em 0. Ex: 'Luis'  L[0], u[1], i[2], s[3] 
print(frase[3]) #Printa somente a letra no indice 3 (No exemplo seria a letra 's')
print(frase[3:13]) #Printa as letras do indice 3 ao 12, o indice 13 é excluido.
print(frase[:13]) #Por não estar indicando o indice inicial, imprime do começo ao 12 (Excluindo o ultimo indice).
print(frase[13:]) #Por não determinar o indice final, imprime a partir do 13º indice ao ultimo.
print(frase[1:15:2]) #Ele vai imprimir na tela do indice 1 ao 13, mas pulando uma letra e imprimindo a proxima ex: "uva" ficaria "UA"
print(frase[1::2]) #Ele imprime do 1 ate o final por não está determinado, mas pulando uma letra e imprimindo a proxima
print(frase[::2]) #Ele vai mostrar do começo ao fim pulando de 2 em 2, excluindo 1 e mostrando o proximo.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("""   
      
      Luis fh fuu df ui gfigaufi g 
    uidf 
                is gduif g
        uisf uisd fiu g
duif giusf 
            ui dfui ui gud gu""")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(frase.count('o')) #O .count conta coisas em especificos por exeplo a letra 'o', ele vai contar a quantidade, e se estiver maiuscula so vai ser contada as maiusculas da mesma forma com as minusculas.
print(frase.upper().count('O'))#O .upper() serve pra colocar em maiusculo. No caso ele está colocando toda a variavel frase em maiusculo.
print(frase.lower().count('o'))#O .lower() serve pra colocar em minusculo. No caso ele está colocando toda a variavel frase em minusculo.
print(len(frase)) #A função len conta quantos indices tem a variavel.


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
frase1 = '   Curso em Vídeo Python   '
print(len(frase1.strip()))#O .strip() tira os espaços indesejados
print(frase1.strip())


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(frase.replace('Pyhton','Android')) #O .replace ele substitui a primeira frase em aspas pela segunda. Mas sem salvar na memoria.
#Para salvar na memoria teria que usar assim " frase = frase.replace('Python', 'Android') "

print('curso' in frase) #Verifica se Tem a palavra curso em frase
print('Curso' in frase1) #Verifica se Tem a palavra Curso em frase

print(frase.find('Video')) #Mostra a posição da palavra. (-1) significa que não existe. Ele diferencia letra maiuscula e minuscula.
print(frase.lower().find('Video')) # .lower diminui toda a frase e o .find já verifica se tem a palavra em minusculo

print(frase.split())#Cria uma lista dividindo a frase

#Após dividir a frase em lista, pede que exiba o item da lista que está na posição 0
dividindo = frase.split()
print(dividindo[0])

#Após dividir a frase em lista, pede que exiba o item da lista que está na posição 2 e a letra q está na posição 3
dividindo = frase.split()
print(dividindo[2][3])#O primeiro couchete mostra a posição da palavra, o segundo couchete mostra qual é a posição da letra q exiba 
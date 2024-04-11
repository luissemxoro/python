v = float(input('Digite o valor do produto: '))
p = int(input('Digite a condição de pagamento:\n [1] Á vista dinheiro/pix: ''10%'' de desconto \n [2] Á vista no cartão: ''5%'' de desconto \n [3] Em até 2x no cartão: preço normal \n [4] 3x ou mais no cartão: ''20%'' de juros.\n Digite sua escolha: '))

if p == 1:
    c = (90 / 100) * v
    #Jeito certo 
    #c = (10/100) * v 
    #v - c 
    print('O valor do produto fica R${:.2f}'.format(c))

elif p == 2:
    c1 = (95 / 100) * v
    print('O valor do produto fica R${:.2f}'.format(c1))

elif p == 3:
    print('O valor do produto permanece R${:.2f}'.format(v))

elif p == 4:
    c2 = (20 / 100) * v
    c3 = c2 + v 
    print('O valor do produto fica R${:.2f}'.format(c3))
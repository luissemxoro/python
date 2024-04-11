d = int(input('\nPor quantos dias o carro foi alugado? '))
q = float(input('Qual foi a quilometragem rodada? '))

vlrd = d * 60
vlrq = q * 0.15
vlrt = vlrq + vlrd

print('-' * 100)
 
print('\nO carro foi alugado por {} dias...........*(R$60,00 p/ dia)*. \nO carro rodou {} Km......................*(R$0,15 p/ Km)*.\n\n ----- O Valor a pagar fica R${:.2f} !\n'.format(d, q, vlrt))
 
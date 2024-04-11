vlr_sal = float(input('Digite o salario: '))
vlr_casa = float(input('Digite o valor da casa: '))
anos = int(input('Em quantos anos a casa será quitada: '))

vlr = 30 * vlr_sal / 100
meses = anos * 12
prest = vlr_casa / meses 

if prest > vlr:
    print ('O emprestimo foi \033[31mNEGADO\033[m, pois a prestação execede os 30%' ' do seu salario!!')
    print('Valor da prestação: {:.2f}\n Salario (30%): {:.2f} '.format(prest, vlr))
else: 
    print('Para o pagamento da casa de {:.2f} em {} anos, terá cada parcela de R${:.2f}, não comprometendo o seu salario\n O emprestimo foi \033[32m APROVADO\033[m'.format(vlr_casa,anos,prest))


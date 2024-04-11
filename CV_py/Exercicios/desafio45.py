import random

pe = 'Pedra'
pa = 'Papel'
te = 'Tesoura'

j = [pe, pa, te]
random.shuffle(j)


jogador = input('Escolha: Pedra, Papel ou Tesoura.\n')
rj = jogador.upper()
print('-'*100)
if j[0] == pe:
    print('MAQUINA: PEDRA')
    if rj == 'PEDRA':
        print('VOCÊ: PEDRA \nVocês \033[33mEMPATARAM!\033[33m')
    elif rj == 'TESOURA':
        print('VOCÊ: TESOURA \nVocê \033[31mPERDEU!\033[m')
    else:
        print('VOCÊ: PAPEL \nVocê \033[32mGANHOU!\033[m')


elif j[0] == pa:
    print('MAQUINA: PAPEL')
    if rj == 'PEDRA':
        print('VOCÊ: PEDRA \nVocê \033[31mPERDEU!\033[m')
    elif rj == 'PAPEL':
        print('VOCÊ: PAPEL \nVocês \033[33mEMPATARAM!\033[33m')
    else: 
        print('VOCÊ: TESOURA \nVocê \033[32mGANHOU!\033[m')


else: 
    print('MAQUINA: TESOURA')
    if rj == 'TESOURA':
        print('VOCÊ: TESOURA \nVocês \033[33mEMPATARAM!\033[33m')
    elif rj == 'PAPEL':
        print('VOCÊ: PAPEL \nVocê \033[31mPERDEU!\033[m')
    else:
        print('VOCÊ: PEDRA \nVocê \033[32mGANHOU!\033[m')







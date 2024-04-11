from datetime import date
atual = date.today().year
n = int(input('Digite o ano em que você nasceu: '))
i = atual - n
print('Quem nasceu em {}, em {} deve ter {} anos'.format(n,atual,i))

if i <= 9:
    print('A sua categoria é MIRIM!')
elif i > 9 and i < 15:
    print('A sua categoria é INFANTIL!')
elif i >= 15 and i <=19:
    print('A sua categoria é JUNIOR!')
elif i == 20:
    print('A sua categoria é SÊNIOR!')
elif i >= 21:
    print('A sua categoria é MASTER!')
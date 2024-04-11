print('\033[7;31;43mOlá Mundo \033[m')

nome = 'luis'

print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;31;43m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7m'}

print('Prazer, {}{}{}.'.format(cores['pretoebranco'],nome,cores['limpa']))
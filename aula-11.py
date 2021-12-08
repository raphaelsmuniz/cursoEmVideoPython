print('Olá mundo!')
nome = 'Raphael'

cor = {'preto' : '\033[30m',
       'azul' : '\033[34m',
       'limpa' : '\033[m'}

print('O meu nome é: {}{}{}'.format(cor['azul'], nome, cor['limpa']))
num = int(input('Escreva um número: '))
baseNum = int(input('Escolha uma dessas opções: \n'
                    '1 - para binário; \n'
                    '2 - para octal; \n'
                    '3 - para hexadecimal. \n'))

#escolha das bases numéricas
if baseNum == 1:
    print('O número {} em binário é {}.'.format(num, bin(num)))
elif baseNum == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)))
elif baseNum == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)))

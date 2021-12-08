print('=-'*8, ' Tabuada ', '-='*8)
print('')

#informando número para a tabuada
num = int(input('digite um número para a tabuada: '))

#calculando e montando a tabuada
for c in range(0, 11):
    tab = c * num
    print('{} x {} = {}'.format(num, c, tab))
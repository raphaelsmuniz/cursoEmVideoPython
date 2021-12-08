print('=-'*8, ' Números primos ', '-='*8)
print('')

num = int(input('Informe um número qualquer: '))

if (num / num == 1) and (num / 1 == num) and (num % 2 == 0) or (num % 2 != 0):
    print('é primo...')
else:
    print('não é primo...')
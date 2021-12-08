
soma = 0
for c in range(1, 7):
    num = int(input('Informe os números: '))

    if num % 2 == 0:
        soma += num

    else:
        print('Número {} é ímpar, logo não servirá!'.format(num))

print('A soma dos números pares é {}'.format(soma))
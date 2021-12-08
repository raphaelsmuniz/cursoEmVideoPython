print('=-'*10, ' Comparando números ', '-='*10)

#informando os números
n1 = int(input('Digite o 1o número: '))
n2 = int(input('Digite o 2o número: '))

#fazendo a comparação
if n1 > n2:
    print('O primeiro valor {} é maior!'.format(n1))
elif n1 < n2:
    print('O segundo valor {} é maior!'.format(n2))
else:
    print('Não existe valor MAIOR, os dois são iguais!')

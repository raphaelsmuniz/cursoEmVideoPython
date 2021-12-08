d = int(input('Informe o número de dias: '))
km = float(input('Informe a quilometragem percorrida: '))
preco = (d * 60) + (km * 0.15)
print('O valor a pagar pelo aluguel é de R$ {:.2f}'.format(preco))
dist = float(input('Informe a distância de sua viagem: '))

if dist <= 200:
    pas = dist * 0.5
    print('O valor da minha passagem é R$ {:.2f} para uma viagem de até 200Km.'.format(pas))
else:
    pas = dist * 0.45
    print('A sua viagem foi acima de 200Km, logo o valor da passagem é de R$ {:.2f}.'.format(pas))

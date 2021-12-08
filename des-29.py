vel = float(input('Informe a velocidade do carro: '))

if vel > 80:
    multa = 7*(vel - 80)
    print('Velocidade acima de 80 Km/h! Logo será multado em R$ {:.2f}'.format(multa))
else:
    print('Parabéns!!! Você está respeitando os limites de velocidade!')

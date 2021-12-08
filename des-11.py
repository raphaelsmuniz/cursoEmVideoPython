larg = float(input('digite a largura da parede: '))
alt = float(input('digite a altura da parede: '))
a = larg * alt
tinta = a / 2
print('As dimensões da parede {:.2f}m e {:.2f}m, formam uma área de {:.2f}m² e a quantidade \n'
      'de tinta necessária é de {:.2f}l.'.format(larg, alt, a, tinta))
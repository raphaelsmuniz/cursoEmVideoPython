from datetime import date

#informando o ano de nascimento
anoNasc = int(input('Informe o ano de nascimento: '))

#calculando a diferença de data
ano = date.today().year - anoNasc

#definindo as categorias
if ano <= 9:
    print('Para a idade de {}, sua categoria é a MIRIM!'.format(ano))
elif 9 < ano <= 14:
    print('Para a idade de {}, sua categoria é a INFANTIL!'.format(ano))
elif 14 < ano <= 19:
    print('Para a idade de {}, sua categoria é a JUNIOR!'.format(ano))
elif ano == 20:
    print('Para a idade de {}, sua categoria é a SÊNIOR!'.format(ano))
elif ano > 20:
    print('Para a idade de {}, sua categoria é a MASTER!'.format(ano))

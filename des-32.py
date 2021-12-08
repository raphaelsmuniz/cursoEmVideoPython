from datetime import date
ano = int(input('Informe o ano para verificação! Ou digite 0 para verificar o ano atual! '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é bissexto!'.format(ano))
else:
    print('Ano {} não é bissexto!'.format(ano))

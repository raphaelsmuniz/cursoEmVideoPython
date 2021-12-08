val = float(input('Digite o valor do produto: '))
desc = (val * 5)/100
vald = val - desc
print('O custo do produto de R$ {:.2f} com 5% de desconto, fica em R$ {:.2f}.'.format(val, vald))
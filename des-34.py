sal = float(input('Informe o seu salário: R$ '))

if sal > 1250.00:
    sal10 = (sal*0.1)+sal
    print('O novo salário é de R$ {:.2f}'.format(sal10))
else:
    sal15 = (sal*0.15)+sal
    print('O novo salário é de R$ {:.2f}'.format(sal15))
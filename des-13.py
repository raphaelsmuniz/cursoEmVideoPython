sal = float(input('Digite o valor do salário: R$ '))
aum = (sal * 0.15)
saln = sal + aum
print('O salário de R$ {:.2f}, teve um aumento de 15% e agora está em R$ {:.2f}.'.format(sal, saln))
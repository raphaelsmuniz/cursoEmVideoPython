print('=-'*5, ' Aprovação de empréstimo bancário ', '-='*5)
print('\n')

#informações iniciais
vlCasa = float(input('Informe o valor da casa: R$ ').strip())
sal = float(input('Informe o valor do salário: R$ ').strip())
tempoA = int(input('Em quantos anos será o financiamento: ').strip())

#valor da prestação da casa e conversão do tempo
tempoM = tempoA * 12
vlPrest = vlCasa / tempoM

#porcentagem do salário
sal30 = sal * 0.3

#verificando a condição de excessão
if vlPrest < sal30:
    print('Empréstimo concedido!')
    print('O valor da prestação será de R$ \033[1;31m{:.2f} \033[mpara um período de \033[1;30m{}\033[m anos.'.format(vlPrest, tempoA))
else:
    print('Empréstimo não concedido! O valor da prestação excede 30% do seu salário!')

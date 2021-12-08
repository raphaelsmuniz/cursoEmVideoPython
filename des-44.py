#capturando o preço e a condição de pagamento
preco = float(input('Informe o valor do produto: R$ '))
print('1 - dinheiro/cheque à vista; \n'
      '2 - cartão à vista; \n'
      '3 - em até 2x no cartão; \n'
      '4 - em 3x ou mais no cartão.')
condPag = int(input('Informe a sua condição de pagamento: '))

#calculando os valores conforme a cond de pagamento
if condPag == 1:
      valFinal = preco - (preco*0.1)
      print('Você escolheu pagar à vista o valor R$ {:.2f}, logo você terá 10% de desconto!'.format(preco), end='')
      print(' Valor final = R$ {:.2f}.'.format(valFinal))

elif condPag == 2:
      valFinal = preco - (preco * 0.05)
      print('Você escolheu à vista no cartão com o valor R$ {:.2f}, logo você terá 5% de desconto!'.format(preco))
      print('Valor final = R$ {:.2f}.'.format(valFinal))

elif condPag == 3:
      valFinal = preco / 2
      print('Você escolheu parcelar em 2x se juros no cartão o valor de R$ {:.2f}, logo não terá desconto!'.format(preco))
      print('Valor final = R$ {:.2f} em 2x.'.format(valFinal))

elif condPag == 4:
      parc = int(input('Informe a quantidade de parcelas: '))
      valJuros = preco + (preco * 0.2)
      valFinal = valJuros / parc
      print('Você escolheu parcelar em {}x no cartão o valor de R$ {:.2f}, logo será acrescido 20% de juros!'.format(parc, preco))
      print('Valor final = R$ {:.2f} em {}x.'.format(valFinal, parc))

else:
    print('Opção inválida de pagamento! Tente novamente...')
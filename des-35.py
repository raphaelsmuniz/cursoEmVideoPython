print('= '*5, 'Condição de existência de um triângulo', ' ='*5)
print('')
#informando os lados do triângulo
a = float(input('Digite a 1a medida do triângulo: '))
b = float(input('Digite a 1a medida do triângulo: '))
c = float(input('Digite a 1a medida do triângulo: '))

#analisando as medidas dos lados
if (abs(b-c) < a < (b+c)) and (abs(a-c) < b < (a+c)) and (abs(a-b) < c < (a+b)):
    print('Com estas medidas informadas {}, {} e {}, podemos dizer que É UM TRIÂNGULO!'.format(a, b, c))
else:
    print('Com estas medidas informadas {}, {} e {}, podemos dizer que NÃO é um triângulo!'.format(a, b, c))

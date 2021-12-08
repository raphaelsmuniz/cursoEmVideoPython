#informando os lados do triângulo
a = float(input('Digite a 1a medida do triângulo: '))
b = float(input('Digite a 2a medida do triângulo: '))
c = float(input('Digite a 3a medida do triângulo: '))

#analisando a existência e o tipo do triângulo
if (abs(b-c) < a < (b+c)) and (abs(a-c) < b < (a+c)) and (abs(a-b) < c < (a+b)):
    print('Com estas medidas informadas {}, {} e {}, podemos dizer que É UM TRIÂNGULO!'.format(a, b, c))

    if a == b == c:
        print('Triângulo Equilátero!')
    elif (a == b) or (b == c) or (a == c):
        print('Triângulo Isósceles!')
    elif a != b != c != a:
        print('Triângulo Escaleno!')

else:
    print('Com estas medidas informadas {}, {} e {}, podemos dizer que NÃO é um triângulo!'.format(a, b, c))

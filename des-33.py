print('='*5, ' Qual é o maior e menor número? ', '='*5)

a = int(input('Informe o 1o número: '))
b = int(input('Informe o 2o número: '))
c = int(input('Informe o 3o número: '))

"""
# Para o número maior:
if a>b and c<a:
    print('O maior número é {}.'.format(a))
elif b>a and c<b:
    print('O maior número é {}.'.format(b))
else:
    print('O maior número é {}.'.format(c))

# Para o número menor:
if a<b and c>a:
    print('O menor número é {}.'.format(a))
elif b<a and c>b:
    print('O menor número é {}.'.format(b))
else:
    print('O menor número é {}.'.format(c))"""

#verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))
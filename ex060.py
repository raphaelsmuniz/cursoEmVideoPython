'''num = int(input('Digite um número: '))

fatorial = num * (num - 1)
aux = fatorial
contador = 0
aux3 = num - 2
c = aux3

while contador < aux3:
    fatorial = fatorial * c
    contador += 1
    c -= 1

print('Calculando {}! = {}'.format(num, fatorial))
'''
#---------------------------------------------------------
'''num2 = int(input('Digite um número: '))

fatorial2 = num2 * (num2 - 1)
fatorial3 = fatorial2
aux2 = num2 - 2

for contador2 in range(aux2, 0, -1):
    fatorial3 = fatorial3 * contador2

print(fatorial3)
'''
'''
from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = factorial(num)
print('O fatorial do número {}! é {}.'.format(num, fatorial))
'''

n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n, end=''))
for c in range(c, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')
'''
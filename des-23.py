from random import randint

#a = str(randint(0, 9999))
#a = input('Digite um número de 4 dígitos: ')
num = int(input('Digite um número: '))

"""print('''
if len(a) == 4:
    print('Unidade: {}'.format(a[3]))
    print('Dezena: {}'.format(a[2]))
    print('Centena: {}'.format(a[1]))
    print('Milhar: {}'.format(a[0]))
elif len(a) == 3:
    print('Unidade: {}'.format(a[2]))
    print('Dezena: {}'.format(a[1]))
    print('Centena: {}'.format(a[0]))
    print('Milhar: {}'.format(0))
elif len(a) == 2:
    print('Unidade: {}'.format(a[1]))
    print('Dezena: {}'.format(a[0]))
    print('Centena: {}'.format(0))
    print('Milhar: {}'.format(0))
elif len(a) == 1:
    print('Unidade: {}'.format(a[0]))
    print('Dezena: {}'.format(0))
    print('Centena: {}'.format(0))
    print('Milhar: {}'.format(0))
else:
    print('Número fora do intervalo! Tente novamente...')
    ''')"""

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
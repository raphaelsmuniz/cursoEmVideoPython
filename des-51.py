print('=-'*8, ' Progressão Aritmética ', '-='*8)
print('')

a1 = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão: '))
n = int(input('Informe a quantidade de termos da PA: '))

lista = []

for c in range(1, n + 1):
    pa = a1 + (c-1)*raz
    lista.append(pa)

print('PA = {}'.format(lista), end="")

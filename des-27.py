nome = input('Digite seu nome completo: ').strip()

n1 = nome.split()
print('O primeiro nome é: {}'.format(n1[0]))

n2 = n1[-1]
#print('O último nome é: {}'.format(n2))
print('O último nome é: {}'.format(n1[len(n1)-1]))
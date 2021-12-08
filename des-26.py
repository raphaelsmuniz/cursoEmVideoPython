txt = input('Digite uma frase: ').strip().lower()

a = txt.count('a')
print('Nesta frase existem {} letras A'.format(a))

b = txt.find('a')
print('Nesta frase a 1a letra A está na posição {}'.format(b))

c = txt.rfind('a')
print('Nesta frase a última letra A está na posição {}'.format(c))

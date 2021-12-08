frase = str(input('Digite uma frase: '))

b = frase.replace(' ','').lower().strip()
c = frase
d = frase
#print(b)

a = b[::-1]
#print(a)
#print(len(b))

e = 0
w = 0

for i in range(0, len(b)):
    if (b[i] != a[i]) > 2:
        e += 1
    else: w += 1
    i += 1

if e > 2:
    print('a frase: {}, não é um palíndromo!'.format(c))
else: print('a frase: {}, é um palíndromo!'.format(d))

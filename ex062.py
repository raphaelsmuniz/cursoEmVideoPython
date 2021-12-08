#EU
print('Gerador de PA')
print('-='*10)
t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
n = 0
termos = t1

print('{}'.format(t1), end='')
while n < 10:
    termos += r
    if n < 9:
        print(' -> ', end='')
        print('{}'.format(termos), end='')
    else:
        print(' -> FIM ', end='')
    n += 1

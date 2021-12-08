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

'''GUANABARA
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

'''
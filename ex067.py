cont = 1
tab = 0
print('-'*40)
num = int(input('Quer ver a tabuada de qual valor? '))
print('-'*40)
while True:
    if num < 0:
        break
    elif cont <= 10:
        tab = num * cont
        print(f'{num} x {cont} = {tab}')
        cont += 1
    elif cont > 10:
        print('-' * 40)
        num = int(input('Quer ver a tabuada de qual valor? '))
        print('-' * 40)
        cont = 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print('========== Sequência de Fibonacci ==========')
num = int(input('Quantos termos você quer mostrar? '))
c = 0
cont = 1
a = 0
b = 1

while num > cont:
    if num == 0:
        print('{} -> '.format(a), end='')
    else:
        if num == 1:
            print('{} -> {} -> '.format(a, b), end='')
    a = b + c
    c = b
    b = a
    print(' {} -> '.format(a), end='')
    cont += 1
print('FIM')
r = 'S'
sexo = ''

while r == 'S':
    sexo = str(input('Digite o sexo: ')).upper()
    if (sexo == 'M') or (sexo == 'F'):
        r = 'S'
    else:
        print('Opção errada!!!!')
        print('Digite-a novamente!!!')
    print('Digite 0 para sair!')
    r = str(input('Deseja continuar? [S/0] ')).upper()

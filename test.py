contdeze = 0
valorS = int(input('Que valor você quer sacar? R$ '))
while True:
    while valorS > 9999:
        valorS = int(input('Valor acima de R$ 10.000,00, favor digite novamente quanto quer sacar: R$ '))
    unid = valorS //1 % 10
    deze = valorS //10 % 10
    cent = valorS //100 % 10
    milh = valorS //1000 % 10
#unidade
    if unid == 0:
        unid = 0
    else:
        if unid <= 9:
            print(f'Total de {unid} cédulas de R$ 1,00')
#dezena
    if cent == 0:
        dezeD = deze % 2
        if deze == 1:
            print(f'Total de {deze} cédulas de R$ 10,00')
        elif deze > 1:
            if dezeD == 0:
                dezeD = deze
                while True:
                    dezeD = dezeD - 2
                    contdeze += 1
                    if dezeD == 0:
                        break
                print(f'Total de {contdeze} cédulas de R$ 20,00')
            else:
                if dezeD != 0:
                    dezeD = deze
                    while True:
                        dezeD = dezeD - 2
                        contdeze += 1
                        if dezeD == 1:
                            break
                print(f'Total de {dezeD} cédulas de R$ 10,00')
                print(f'Total de {contdeze} cédulas de R$ 20,00')


        '''else:
            if deze == 5:
                print(f'Total de {cent + 1} cédulas de R$ 50,00')
            else:
                if deze >= 6:
                    deze = deze - 5
                    dezeD = cent + 1
                    print(f'Total de {deze} cédulas de R$ 10,00')
                    print(f'Total de {dezeD} cédulas de R$ 50,00')'''
    break

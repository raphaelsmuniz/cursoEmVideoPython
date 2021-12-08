print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

while True:
    valorS = int(input('Que valor você quer sacar? R$ '))
    unid = valorS //1 % 10
    deze = valorS //10 % 10
    cent = valorS //100 % 10
    milh = valorS //1000 % 10
#unidade
    if unid == 0:
        unid = 0
    else:
        if unid <= 9:
            print(f'são {unid} de 1')
#dezena
    if (1<= deze <= 4):
        print(f'são {deze} de 10')
    else:
        if deze == 5 and cent == 0:
            print(f'são {cent + 1} de 50')
        else:
            if (6<= deze <= 9) and cent == 0:
                deze = deze - 5
                dezeD = cent + 1
                print(f'são {deze} de 10')
                print(f'são {dezeD} de 50')
#centena
    centC = 0
    if cent >= 1 and milh == 0:
        centC = (cent * 100) / 50
        if deze == 5:
            centC = centC + 1
        elif deze > 5:
            dezeC = deze - 5
            centC = centC + 1
            print(f'são {dezeC:.0f} de 10')
        print(f'são {centC:.0f} de 50')
#milhar
    if milh >= 1:
        milhM = (milh * 1000) / 50
        if cent >= 1:
            centM = (cent * 100) / 50
            if deze == 5:
                centM = centM + 1
            elif deze > 5:
                dezeM = deze - 5
                centM = centM + 1
                print(f'são {dezeM:.0f} de 10')
            milhM = milhM + centM
        print(f'são {milhM:.0f} de 50')
    break
    '''if valorS > 9999:
        valorS = int(input('Favor digitar novamente: '))
        

valor = int(input('que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
	if total >= ced:
		total -= ced
		totced += 1
	else:
		if totced > 0:
			print(f'total de {totced} cédulas de R${ced}')
		if ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		totced = 0
		if total == 0:
			break
print('='*30)
print('Volte sempre ao BANCO CEV!!!')'''

print('-'*30)
print('Loja Super Baratão')
print('-'*30)
totC = quantP = 0
menorP = 1
baratoP = ''
while True:
    nomeP = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    totC += preco
    if preco > 1000:
        quantP += 1
    if quantP == 1:
        menorP = preco
    else:
        if preco < menorP:
            menorP = preco
            baratoP = nomeP
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-'*10, ' FIM DO PROGRAMA ', '-'*10)
print(f'O total da compra foi de R$ {totC:.2f}.')
print(f'Temos {quantP} produtos custando custando mais de R$ 1000,00.')
print(f'O produto mais barato foi {baratoP} que custa R$ {menorP:.2f}.')
from random import randint
result = ()
for num in range(1,6):
    numAle = randint(0, 10)
    result += (numAle,)
resultxt = str(result)
txt = resultxt.replace(',', ' ')
txt2 = txt.replace('(', '')
txt3 = txt2.replace(')', '')
print(f'Os valores sorteados foram: {txt3}')
maior = menor = 0
for pos, escnum in enumerate(result):
    if pos == 0:
        maior = menor = escnum
    else:
        if escnum > maior:
            maior = escnum
        if escnum < menor:
            menor = escnum
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
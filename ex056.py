maior = 0
menor = 0
idade = 0
nome = ''

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    a = str(input('Nome: '))
    b = int(input('Idade: '))
    idade += b
    d = str(input('Sexo [M/F]: ')).upper()
    if (c == 1) and (d == 'M'):
        maior = b
        nome = a
    else:
        if (b > maior) and (d == 'M'):
            maior = b
            nome = a
    if (b < 20) and (d == 'F'):
        menor += 1

media = (idade / 4)
print('A média de idade do grupo é de {:2} anos. O homem \n'
      'mais velho é {} com {} anos e houveram {} mulheres \n'
      'abaixo de 20 anos.'.format(media, nome, maior, menor))

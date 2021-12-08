pergunta = 'n'
soma = cont = me = ma = 0
num = int(input('Digite um número: '))
while pergunta != 'N':
    soma += num
    if soma == num:
        ma = me = num
    else:
        if num > ma:
            ma = num
        if num < me:
            me = num
    pergunta = str(input('Deseja continuar? [S - sim / N - não] ')).upper()
    cont += 1
    if pergunta == 'S':
        num = int(input('Digite um número: '))
media = (soma / cont)
print('A soma dos números é {} para {} números digitados, logo a média é {:.2f}.'.format(soma, cont, media))
print('O maior número é {} e o menor é {}.'.format(ma, me))

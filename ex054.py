from datetime import date
ano = date.today().year

a2 = 0
a3 = 0
for c in range(1, 8):
    p = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if (ano - p) <= 21:
        a2 += 1
    else:
        a3 += 1
    c += 1

print('\n{} pessoas ainda não atingiram a maioridade,'.format(a2))
print('e {} pessoas já passaram dos 21 anos de idade.'.format(a3))

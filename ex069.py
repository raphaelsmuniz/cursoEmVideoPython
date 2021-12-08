print('-'*30)
print('     CADASTRE UMA PESSOA')
print('-'*30)
ci = cs = cm = 0
while True:
    idade = input('Idade: ')
    while idade != str():
        idade = input('Idade: ')
        if idade == int():
            break
    int(idade)
    sexo = str(input('Sexo: [M/F] ')).strip()[0].upper()
    print('-'*30)
    if idade > 18:
        ci += 1
    if sexo == 'M':
        cs += 1
    if (sexo == 'F') and (idade < 20):
        cm += 1
    quer = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    if quer == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {ci}')
print(f'Ao todo temos {cs} homens cadastrados')
print(f'E temos {cm} mulheres com menos de 20 anos.')
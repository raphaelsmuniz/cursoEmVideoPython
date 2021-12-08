from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
#comp = randint(0, 10)
soma = res = cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0, 10)
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-'*40)
    soma = jogador + comp
    res = soma % 2
    if res == 0 and opcao == 'P':
        print(f'Você jogou {jogador} e o computador {comp}. Total de {soma} DEU PAR')
        print('-' * 40)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
    if res != 0 and opcao == 'I':
        print(f'Você jogou {jogador} e o computador {comp}. Total de {soma} DEU ÍMPAR')
        print('-' * 40)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
    if (res == 0 and opcao == 'I') or (res != 0 and opcao == 'P'):
        print('Você PERDEU!')
        print('=-' * 40)
        break
    cont += 1

print(f'GAME OVER! Você venceu {cont} vezes.')
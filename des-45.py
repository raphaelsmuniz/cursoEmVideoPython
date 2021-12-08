from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))

print('''Suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura ''')

jogador = int(input('Qual é a sua jogada? '))

print('jo')
sleep(1)
print('ken')
sleep(1)
print('pô!!!')
sleep(1)

print('-='*11)
print('computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada inválida')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada inválida')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada inválida')

from random import randint
from time import sleep

print('====== Computador pensando em um número... ======')
print('')
pc = randint(0,5)

hum = int(input('Usuário, informe um número... '))
print('PROCESSANDO...')
sleep(3)

if pc == hum:
    print('Parabéns Usuário! Você venceu!')
    print('Usuário: {} x {} Computador'.format(hum, pc))
else:
    print('Que pena, o computador venceu!')
    print('Usuário {} x {} Computador'.format(hum, pc))

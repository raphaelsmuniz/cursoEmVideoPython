from random import choice
no1 = input('Digite o 1o nome: ')
no2 = input('Digite o 2o nome: ')
no3 = input('Digite o 3o nome: ')
no4 = input('Digite o 4o nome: ')
lista = choice([no1, no2, no3, no4])
print('O nome dos 4 alunos são: {}, {}, {} e {}.'.format(no1, no2, no3, no4))
print('O nome do escolhido para apagar o quadro é {}.'.format(lista))
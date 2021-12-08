from random import sample
no1 = input('Informe o 1o aluno: ')
no2 = input('Informe o 2o aluno: ')
no3 = input('Informe o 3o aluno: ')
no4 = input('Informe o 4o aluno: ')
lista = sample([no1, no2, no3, no4], k=4)
print('Os 4 alunos são: {}, {}, {} e {}.'.format(no1, no2, no3, no4))
print('A ordem de apresentação é: {}.'.format(lista))
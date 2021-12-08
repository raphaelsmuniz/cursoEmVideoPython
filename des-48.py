print('=-'*8, ' Números ímpares que são múltiplos de 3 ', '-='*8)
print('')

lista = list(range(1, 501))

soma = 0
cont = 0

for c in lista:
    if (c % 2) != 0 and (c % 3) == 0:
        cont += 1
        soma += c
print('A soma dos {} números no intervalo de 1 a 500 é {}.'.format(cont, soma))
n = input('Digite algo: ')
print('É um número? {}'.format(n.isnumeric()))
print('É maiúsculo? {}'.format(n.isupper()))
print('É minúsculo? {}'.format(n.islower()))
print('É alfanumérico? {}'.format(n.isalpha()))
print('É um título? {}'.format(n.istitle()))
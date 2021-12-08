idade = input('Idade: ')
while idade != str():
    idade = input('Idade: ')
    if idade == type(idade):
        break
int(idade)
print(type(idade), idade)

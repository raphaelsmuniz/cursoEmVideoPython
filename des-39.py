from datetime import date

print('=-'*10, ' Alistamento Militar ', '-='*10)

#informando os dados iniciais
nome = str(input('Informe o seu nome completo: ').strip())
sexo = str(input('Informe o sexo: ').strip())
ano = int(input('Informe ano de nascimento: ').strip())

#calculando o tempo
tempo = date.today().year - ano
tempoAlist = abs(tempo - 18)

#escolha do sexo
if sexo.lower() == 'f':
    print('A Srta {} não é obrigada a se alistar!'.format(nome.title()))

elif sexo.lower() == 'm':

#escolha do alistamento
    if tempo < 18:
        print('{}, você ainda irá de alistar! Restam {} anos!'.format(nome.title(), tempoAlist))

    elif tempo == 18:
        print('Parabéns {}! Você completou {} anos e já está na hora de se alistar!'.format(nome.title(), tempo))

    elif tempo > 18:
        print('{}, você já passou {} anos do tempo de alistamento!'.format(nome.title(), tempoAlist))

#informando as notas
n1 = float(input('Informe a 1a nota do aluno: '))
n2 = float(input('Informe a 2a nota do aluno: '))

#calculando as médias
media = (n1 + n2)/2

#informando a situação
if media < 5:
    print('Estude um pouco mais!!! Sua média foi {:.2f} e ficou como reprovado!'.format(media))
elif 5 <= media <= 6.9:
    print('Você está em recuperação!!! Sua média foi {:.2f}.'.format(media))
elif media >= 7:
    print('Parabéns!!! Você foi aprovado com a média {:.2f}.'.format(media))

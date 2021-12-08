#capturando o peso e a altura
peso = float(input('Informe o seu peso: '))
alt = float(input('Informe a sua altura: '))

#calculando o IMC
vlIMC = peso / pow(alt,2)

#analisando o status do IMC
if vlIMC <= 18.5:
    print('Você está abaixo do peso! IMC= {:.1f}'.format(vlIMC))
elif 18.5 < vlIMC <= 25:
    print('Você está no peso ideal! IMC= {:.1f}'.format(vlIMC))
elif 25 < vlIMC <= 30:
    print('Você está com sobrepeso! IMC= {:.1f}'.format(vlIMC))
elif 30 < vlIMC <= 40:
    print('Você está no nível de obesidade! IMC= {:.1f}'.format(vlIMC))
elif vlIMC > 40:
    print('Você está no nível de obesidade mórbida! IMC= {:.1f}'.format(vlIMC))

numExt = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Digite um número entre 0 e 20: '))
while (num < 0) or (num > 20):
    num = int(input('Tente novamente! Digite um número entre 0 e 20: '))
for pos, escolhido in enumerate(numExt):
       if pos == num:
           break
print(f'Você digitou o número {escolhido}')

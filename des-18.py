from math import sin, cos, tan, radians
ang = int(input('Informe um número: '))
x = radians(ang)
sen = sin(x)
coss = cos(x)
tg = tan(x)
print('Os referidos valores são: seno {} é {:.2f}, cosseno {} é {:.2f} e tangente {} é {:.2f}.'.format(ang, sen, ang, coss, ang, tg))
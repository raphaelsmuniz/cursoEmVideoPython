times = 'Sport', 'Bahia', 'São Paulo', 'Santos', 'Corinthians', 'Palmeiras', 'Flamengo', 'Fluminense', 'Botafogo', 'Vasco', 'Cruzeiro', 'Atlético Mineiro', 'Grêmio', 'Internacional', 'Paraná', 'Coritiba', 'Avaí', 'Figueirense', 'Vitória', 'Chapecoense'
print('-='*30)
print(f'Lista de times do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
for pos, chape in enumerate(times):
    if chape == 'Chapecoense':
        colocacao = pos + 1
        break
print(f'A Chapecoense está na {colocacao}ª posição!')

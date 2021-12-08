cid = input('Digite o nome da cidade: ').strip()
"""a = cid.strip().split()
if a[0] == 'Santo':
    print('Esta cidade começa com Santo.')
else:
    print('Esta cidade não começa com Santo.')"""

print(cid[:5].upper() == 'SANTO')
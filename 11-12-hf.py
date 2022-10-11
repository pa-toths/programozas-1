egyikszam=int(input('kérem az első számot 1-100-ig:'))
masikkszam=int(input('kérem az második számot 1-100-ig:'))
if egyikszam==masikkszam:
    print('megegyezik')
elif egyikszam>masikkszam:
    print('Az első szám', egyikszam-masikkszam, 'nagyobb')
elif egyikszam<masikkszam:
    print('Az második szám', masikkszam-egyikszam, 'nagyobb')

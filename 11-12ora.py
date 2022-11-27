gondoltam_szam = 4
print(type(gondoltam_szam))
tipp = int(input('Gondoltam egy számra. Tippeld meg!'))
if tipp == gondoltam_szam:
    print('Ügyes!')  #igaz utasítás
if tipp > gondoltam_szam:
    print('ha nagyobb mint a gondolt szám')
if tipp < gondoltam_szam:
    print('ha kisseb mint a gondolt szám')
print('Pápá')

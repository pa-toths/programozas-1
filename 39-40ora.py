lista = [12,5,4,8,9,11,10,13,6]

def szelsoertekek():
    min_10D = lista[0]
    max_10D = lista[0]
    for szam in lista:
        if szam < min_10D:
            min_10D = szam
        if szam > max_10D:
            max_10D = szam

    print('A legkisebb szám a listában',min_10D)
    print('A legnagyobb szám a listában',max_10D)

szelsoertekek()

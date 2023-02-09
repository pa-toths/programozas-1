"""
def menut_kiir(tipus):
    '''
    A menü megjelenítése a képernyőn
    '''
    if tipus == 2:
        print('1 Új adat bevitele')
        print('3 Kilépés a programból')
    if tipus == 3:
        print('1 Új adat bevitele')
        print('2 Adatok módosítása / törlése')
        print('3 Kilépés a programból')

menut_kiir(2)

"""


def koszont():
    print('Üdv a fedélzeten!')

def koszont_nevel(nev):
    print(f'Szia { nev } ,üdv a fedélzeten!')
koszont_nevel('Ádám')

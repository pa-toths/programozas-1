# A python lista

lista = ["alma","banán","cseresznye"]
print(lista)

lista = ["alma","banán","cseresznye","alma","banán"]
print(lista)
print(lista[0])
print(lista[3])

lista = ["alma","banán","cseresznye","alma","banán"]
print(len(lista))
hossza = len(lista)
print(hossza)

lista1 = ["alma","banán","cseresznye","alma","banán"] # string
lista2 = [1, 5, 7, 9, 3] # int
lista3 = [True, False, False] # bool

lista1 = ["abc", 34, True, 40, "férfi"]
print(lista1)

lista5 = ["alma", "banán", "cseresznye"]
print(type(lista5))
# <class 'list'>

lista = list(("alma", "banán", "cseresznye"))
print(lista)
# nem dolgozatt feladatt

lista = ["alma", "banán", "cseresznye"]
print(lista[1])

# írasuk ki a lista utolsó elemét
lista = ["alma", "banán", "cseresznye"]
print(lista[-1])
print(lista[2])

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5"]
print(lista[2:5])

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[:4])

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[2:])
ujlista = lista[2:]
print(ujlista)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

lista_10D_1csop = []
lista_10D_1csop = ["FB", "GM", "HK", "KG", "MM", "OA", "PJ", "PP", "SP", "SK", "SZM12", "TM", "TT", "TH"]

csop1 = []
csop2 = []
csop3 = []

csop1 = lista_10D_1csop [0:5]
csop2 = lista_10D_1csop [5:10]
csop3 = lista_10D_1csop [10:]
print(csop1)
print(csop2)
print(csop3)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[-4:-1])

lista_10D_1csop = []
lista_10D_1csop = ["FB", "GM", "HK", "KG", "MM", "OA", "PJ", "PP", "SP", "SK", "SZM12", "TM", "TT", "TH"]
megbukottak_lista  = ["SZM12", "TM", "TT", "TH"]
print(megbukottak_lista,"megbuktak")

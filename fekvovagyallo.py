szél = int(input("Adja meg a téglalap szélességét:"))
mag = int(input("Adja meg a téglalap magasságát:"))
T = szél * mag
if mag > szél:
    print("Ez egy álló téglalap és a területe" , T)
elif szél > mag:
    print("Ez egy fekvő téglalap és a területe" , T)
elif szél == mag:
    print("Ez egy négyzet és a területe" , T)

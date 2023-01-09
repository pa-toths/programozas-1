szél = int(input("Adja meg a téglalap szélességét:"))
mag = int(input("Adja meg a téglalap magasságát:"))
if mag > szél:
    print("Ez egy álló téglalap és a területe" , mag * szél)
elif szél > mag:
    print("Ez egy fekvő téglalap és a területe" , szél * mag)
elif szél == mag:
    print("Ez egy négyzet és a területe" , szél * mag)

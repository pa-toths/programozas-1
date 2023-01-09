 név = input("Kérem a teljes nevét:")
év = int(input("Kérem az élet korát:"))
if év < 2:
    print("Magga még csecsemő")
elif év < 5:
    print("Magga még kisgyerek")
elif év < 12:
    print("Magga még gyerek")
elif év < 16:
    print("Magga még serdülő")
elif év < 25:
    print("Magga már ifjú")
elif év < 65:
    print("Magga már felnőtt")
elif év > 65:
    print("Magga már nyugdíjas")

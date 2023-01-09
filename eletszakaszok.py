név = input("Kérem a teljes nevét:")
év = int(input("Kérem az élet korát:"))
if év < 2:
    print(név , "Magga még csecsemő")
elif év < 5:
    print(név , "Magga még kisgyerek")
elif év < 12:
    print(név , "Magga még gyerek")
elif év < 16:
    print(név , "Magga még serdülő")
elif év < 25:
    print(név , "Magga már ifjú")
elif év < 65:
    print(név , "Magga már felnőtt")
elif év > 65:
    print(név , "Magga már nyugdíjas")

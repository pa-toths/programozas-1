név = input("Kérem a teljes nevét: ")
év = int(input("Kérem az élet korát: "))
if év < 2:
    print("A kora alapján", név , "csecsemő!")
elif év < 5:
    print("A kora alapján", név , "kisgyerek!")
elif év < 12:
    print("A kora alapján", név , "gyerek!")
elif év < 16:
    print("A kora alapján", név , "serdülő!")
elif év < 25:
    print("A kora alapján", név , "ifjú!")
elif év < 65:
    print("A kora alapján", név , "felnőtt!")
else:
    print("A kora alapján", név , "nyugdíjas!")

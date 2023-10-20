import random

print("")
print("*** Batu-Gunting-Kertas ***")
print("---------------------------")

print("1.gunting")
print("2.batu")
print("3.kertas")
print("---------------------------")

tipe = input("Pilih gunting/batu/kertas: ")

if tipe in ("gunting", "batu", "kertas"):
    pilih = ("gunting", "batu", "kertas")
    bot_random = random.choice(pilih)
    print(tipe, "lawan" ,bot_random)
    print("---------------------------")

    if tipe == bot_random:
        print("Wah!!! Seri")
    else:
        if tipe == 'batu':
            if bot_random == 'gunting':
                print("Selamat Anda Menang")
            if bot_random == 'kertas':
                print("Yahh, Anda Kalah :(")

        if tipe == 'kertas':
            if bot_random == 'batu':
                print("Selamat Anda Menang")
            if bot_random == 'gunting':
                print("Yahh, Anda Kalah :(")
        
        if tipe == 'gunting':
                    if bot_random == 'kertas':
                        print("Selamat Anda Menang")
                    if bot_random == 'batu':
                        print("Yahh, Anda Kalah :(")
                

print("")
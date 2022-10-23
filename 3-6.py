import random
angka_rahasia=random.randrange(0,10)
limit=True

while limit:
    angka_tebak=int(input("Masukkan angka (1-9) : "))
    if angka_tebak==angka_rahasia:
        print("Tebakanmu benar")
        print("Selamat, kamu menang")
        break
    elif angka_tebak>angka_rahasia:
        print("Angka tebakan lebih besar")
    elif angka_tebak<angka_rahasia:
        print("angka tebakan lebih kecil")
suku_awal=float(input("Masukkan suku pertama\t: "))
banyak_suku=int(input("Masukkan jumlah suku\t: "))
rasio=float(input("Masukkan rasio\t\t: "))
for i in range(1,banyak_suku+1):
    suku=suku_awal*(rasio**(i-1))
    print(f"Suku ke-{i} = {suku}")
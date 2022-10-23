bil=[]
n=int(input("Berapa bilangan yang ingin anda masukkan : "))
for i in range(0,n):
    bil.append(int(input(f"masukan bilangan ke-{i+1} : ")))
total=sum(bil)
rerata=total/n
print(f"Jumlah seluruh bilangan = {total}")
print(f"Rata-rata = {rerata}")

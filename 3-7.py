bil=[]
x=int(input("x\t= "))
y=int(input("y\t= "))
for i in range(x+1,y):
    bil.append(i)
bil1=bil.pop(0)
bil2=bil.pop(0)
bil3=bil.pop(0)
bil4=bil.pop(0)
bil5=bil.pop(0)
jumlah=sum(bil)
print(f"deret\t= {bil1} {bil2} {bil3} {bil4} {bil5}")
print(f"jumlah\t= {jumlah}")
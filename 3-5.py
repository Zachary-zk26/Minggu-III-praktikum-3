x=int(input())
def faktorial(x):
    hasil=1
    for i in range(2,x+1):
        hasil*=i
    return hasil
print(faktorial(x))
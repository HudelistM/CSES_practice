n=int(input())
rez=n
counter=0

while rez!=0:
    l=list(map(int,str(rez)))
    if (rez!=0):
        counter+=1
    rez-=max(l)
print(counter)
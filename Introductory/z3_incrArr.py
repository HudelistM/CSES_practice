n=int(input())
l=[int(x) for x in input().split(" ")]
counter=0
for i in range(1,len(l)):
    if(l[i-1]>l[i]):
        counter+=(l[i-1]-l[i])
        l[i]=l[i-1]
print(counter)
print(l)



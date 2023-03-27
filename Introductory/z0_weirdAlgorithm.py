n=int(input())
rez=[]
rez.append(n)
while(n!=1):
    if(n%2==0):
        n=int(n/2)
        rez.append(n)
    elif(n%2!=0):
        n=int((n*3)+1)
        rez.append(n)
print(' '.join(map(str,rez)))
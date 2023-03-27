n=int(input())
for i in range(n):
    a,b=map(int,input().split(" "))
    
    if(max(a,b))>2 * min(a,b):
        print("NO")
    elif((a+b)%3==0):
        print("YES")
    else:
        print("NO")

def coinPiles(n):
    a,b=map(int,input().split(" "))
    if (max(a,b))>2 * min(a,b):
        print("NO")
    elif((a+b)%3==0):
        print("YES")
    else:
        print("NO")
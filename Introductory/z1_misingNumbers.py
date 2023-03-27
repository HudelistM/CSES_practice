n=int(input())
l=[int(x) for x in input().split(" ")]
total = int((n*(n+1))/2)
sumaL=sum(l)
print(total-sumaL)
import sys
input=sys.stdin.readline
 
n,m = map(int,input().split())
e=[[int(t) for t in input().split()] for _ in range(m)]
d=[10**15]*(n+1)
p=[0]*(n+1)
 
def bt(i):
    path=[i]
    v=[0]*(n+1)
    ind=[0]*(n+1)
    j=0
    while not v[i]:
        v[i]=1
        ind[i]=j
        i=p[i]
        path.append(i)
        j+=1
    return reversed(path[ind[i]:])
 
ans=0
for i in range(n):
    for a,b,c in e:
        if d[b]>d[a]+c:
            d[b]=d[a]+c
            p[b]=a
            if i==n-1:
                ans=1
                print('YES',*bt(b))
                break
 
if not ans:
    print('NO')
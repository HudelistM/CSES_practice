
import sys
sys.setrecursionlimit(200001)
n,m = map(int,input().split())
p = [[i,1] for i in range(n+1)]

def find(r):
    if r!=p[r][0]: p[r] = find(p[r][0])
    return p[r]

a,b = n,1
for i in range(m):
    u,v = map(int,input().split())
    u,v = find(u)[0],find(v)[0]
    if u!=v:
        p[u][1] += p[v][1]
        p[v][0] = u
        b = max(b,p[u][1])
        a -= 1
    print(a,b)
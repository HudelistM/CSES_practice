n, m = map(int, input().split()) 
 
edges = []
 
for i in range(m): 
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, c)) 
 
edges.sort(key = lambda x: x[2])
 
link = [i for i in range(n)] 
size = [i for i in range(n)]

def find(x):
    while x != link[x]:
      x = link[x] 
    return x 
  
def same(a, b): 
    return find(a) == find(b)  
 
def unite(a, b): 
    a = find(a) 
    b = find(b)
    if size[a] < size[b]: 
      temp = b 
      b = a 
      a = temp
    size[a] += size[b] 
    link[b] = a 
 
costs = 0
roads = 0
 
for a, b, c in edges: 
    if not same(a, b):
      unite(a, b)
      costs += c  
      roads += 1
 
if roads != n - 1:
    print("IMPOSSIBLE") 
else:
    print(costs)
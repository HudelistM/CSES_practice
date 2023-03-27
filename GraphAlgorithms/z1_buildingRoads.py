from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
adj = defaultdict(list)
visited = [False] * (n+1)
bridges = []

def DFS(node):
    visited[node] = True
    for child in adj[node]:
        if not visited[child]:
            DFS(child)

for i in range(m):
    node1, node2 = map(int, input().split())
    adj[node1].append(node2)
    adj[node2].append(node1)


for i in range(1, n+1):
    if not visited[i]:
        bridges.append(i)
        DFS(i)

print(len(bridges)-1)
for i in range(len(bridges)-1):
    print(bridges[i], bridges[i+1])
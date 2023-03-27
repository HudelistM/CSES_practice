import heapq

INF = int(1e18)
N = 2 * 10 ** 5 + 3

adj = [[] for _ in range(N)]
dist = [INF] * N
pq = []

def dijkstra():
    dist[1] = 0
    heapq.heappush(pq, (0, 1))
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        for c, v in adj[u]:
            if dist[v] <= c + d:
                continue
            dist[v] = c + d
            heapq.heappush(pq, (dist[v], v))

n, m = map(int, input().split())
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((w, b))
dijkstra()
for i in range(1, n+1):
    print(dist[i], end=" ")
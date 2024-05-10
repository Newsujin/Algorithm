import sys
import heapq


N, M = map(int, sys.stdin.readline().split())
INF = float('inf')
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append((b, c))
    edge[b].append((a, c))


def dijkstra(start):
    distances = [INF for _ in range(N + 1)]
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        distance, now = heapq.heappop(q)
        if distance > distances[now]:
            continue
        for node, cost in edge[now]:
            if distance + cost < distances[node]:
                distances[node] = distance + cost
                heapq.heappush(q, (distance + cost, node))
    return distances[N]


print(dijkstra(1))
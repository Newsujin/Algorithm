import sys
import heapq


N, M = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append((b, c))
    edge[b].append((a, c))


INF = float('inf')
def dijkstra(start):
    graph = [INF for _ in range(N + 1)]
    graph[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        distance, now = heapq.heappop(heap)
        if graph[now] < distance: continue

        for node, cost in edge[now]:
            if graph[node] > distance + cost:
                graph[node] = distance + cost
                heapq.heappush(heap, (distance + cost, node))

    return (graph[N])


print(dijkstra(1))
import sys, heapq

INF = float('INF')

def dijkstra(base, n, k, edges):
    q = []
    heapq.heappush(q, (0, 1))
    dist = [INF for _ in range(n + 1)]
    dist[1] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue

        for (next, nextDist) in edges[now]:
            cost = d
            if nextDist > base:
                cost += 1
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (cost, next))

    return dist[n] <= k



def binary_search(n, p, k, edges):
    left, right = 0, 1000000
    res = -1

    while left <= right:
        mid = (left + right) // 2
        if dijkstra(mid, n, k, edges):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return res


n, p, k = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n + 1)]
for _ in range(p):
    n1, n2, cost = map(int, sys.stdin.readline().split())
    edges[n1].append((n2, cost))
    edges[n2].append((n1, cost))

result = binary_search(n, p, k, edges)
print(result)
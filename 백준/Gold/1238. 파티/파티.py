import sys, heapq

input = sys.stdin.readline
n, m, x = map(int, input().split())
city = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    city[a].append((b, t))


def dijkstra(start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue

        for node_idx, node_cost in city[now]:
            cost = dist + node_cost
            if distance[node_idx] > cost:
                distance[node_idx] = cost
                heapq.heappush(q, (cost, node_idx))

    return distance


result = 0
for i in range(1, n + 1):
    go = dijkstra(i)[x]
    back = dijkstra(x)[i]
    result = max(result, go + back)


print(result)
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    hq = []
    distance[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        now_dist, now = heapq.heappop(hq)
        
        if distance[now] < now_dist:
            continue
        
        for next, cost in bus[now]:
            new_dist = now_dist + cost
            if new_dist < distance[next]:
                distance[next] = new_dist
                heapq.heappush(hq, (new_dist, next))

dijkstra(start)
print(distance[end])
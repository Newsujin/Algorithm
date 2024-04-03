import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0,0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] >= 1:
                    graph[ny][nx] += 1
                else:
                    visited[ny][nx] = True
                    q.append([nx, ny])

def melt_cheese():
    melted = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                melted = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    return melted

hour = 0
while True:
    bfs()
    if melt_cheese():
        hour += 1
    else:
        break

print(hour)
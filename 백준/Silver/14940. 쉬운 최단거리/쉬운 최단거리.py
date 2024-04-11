import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]


visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x):
    maps[y][x] = 0
    visited[y][x] = True
    q = deque([(x, y, 1)])
    
    while q:
        x, y, distance = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and not visited[ny][nx]:
                maps[ny][nx] = distance
                visited[ny][nx] = True
                q.append((nx, ny, distance + 1))

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] == 1:
                maps[i][j] = -1

    for line in maps:
        print(*line)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            x, y = i, j
            break

bfs(x, y)
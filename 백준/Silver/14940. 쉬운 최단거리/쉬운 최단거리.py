import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = 1
    maps[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny <m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1


for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            x, y = i, j
            break

bfs(x, y)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            maps[i][j] = -1

for line in maps:
    print(*line)
import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_island(y, x, cnt):
    q = deque([(x, y)])
    visited[y][x] = True
    maps[y][x] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] and not visited[ny][nx]:
                maps[ny][nx] = cnt
                q.append((nx, ny))
                visited[ny][nx] = True

def find_path(island):
    q = deque([])
    distance = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == island:
                q.append((j, i))
                distance[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[ny][nx] != island and maps[ny][nx] != 0:
                    return distance[y][x]
                if maps[ny][nx] == 0 and distance[ny][nx] == -1:
                    distance[ny][nx] = distance[y][x] + 1
                    q.append((nx, ny))
    
    return sys.maxsize

cnt = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] and not visited[i][j]:
            cnt += 1
            find_island(i, j, cnt)

min_distance = sys.maxsize
for island in range(1, cnt + 1):
    min_distance = min(min_distance, find_path(island))

print(min_distance)
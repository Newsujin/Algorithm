import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    ice = deque([(x, y)])
    while ice:
        x, y = ice.popleft()
        visited[y][x] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] != 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    ice.append((nx, ny))
                elif graph[ny][nx] == 0:
                    sea_cnt[y][x] += 1
    return 1

day = 0
while True:
    iceberg = 0
    visited = [[False] * M for _ in range(N)]
    sea_cnt = [[0] * M for _ in range(N)]
    # 빙산의 개수 세기
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                iceberg += bfs(i, j)

    # 빙산 깎기
    for i in range(N):
        for j in range(M):
            graph[i][j] -= sea_cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    if iceberg == 0:
        day = 0
        break
    if iceberg >= 2:
        break
    day += 1

print(day)
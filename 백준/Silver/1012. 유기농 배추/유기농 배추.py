import sys
sys.setrecursionlimit(10**7)

def dfs(x, y, field, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(field) and 0 <= ny < len(field[0]):
            if field[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny, field, visited)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    worm_cnt = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j, field, visited)
                worm_cnt += 1
    print(worm_cnt)
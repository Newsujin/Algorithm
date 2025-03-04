n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
complex_sizes = []

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            complex_sizes.append(cnt)

complex_sizes.sort()
print(len(complex_sizes))
for size in complex_sizes:
    print(size)
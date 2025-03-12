import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, h):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, h)
    

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_h = max(map(max, graph))
max_safe_zone = 0

for h in range(max_h + 1):
    visited = [[False] * n for _ in range(n)]
    safe_zone_cnt = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, h)
                safe_zone_cnt += 1
    
    max_safe_zone = max(max_safe_zone, safe_zone_cnt)

print(max_safe_zone)
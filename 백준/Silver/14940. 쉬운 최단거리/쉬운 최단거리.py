from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny <m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

n, m = map(int, input().split())
x, y = 0, 0

visited = [[0 for _ in range(m)] for _ in range(n)]
graph = []

for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
            break

bfs(x, y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            graph[i][j] = -1

for line in graph:
    print(*line)
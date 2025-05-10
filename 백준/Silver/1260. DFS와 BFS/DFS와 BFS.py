from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

dfs_res = []
def dfs(start):
    visited[start] = True
    dfs_res.append(start)
    for next in graph[start]:
        if not visited[next]:
            dfs(next)

bfs_res = []
def bfs(start):
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    bfs_res.append(start)
    q = deque([start])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                bfs_res.append(next)

dfs(v)
bfs(v)
print(*dfs_res)
print(*bfs_res)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, i, visited):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)
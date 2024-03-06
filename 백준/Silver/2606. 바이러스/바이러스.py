n = int(input())
computers = [[] for _ in range(n + 1)]
connect = int(input())
for _ in range(connect):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [False] * (n + 1)

def dfs(i):
    visited[i] = True
    for j in computers[i]:
        if not visited[j]:
            dfs(j)

dfs(1)
print(sum(visited) - 1)
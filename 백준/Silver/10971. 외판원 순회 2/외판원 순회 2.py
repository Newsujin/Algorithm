N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')

def dfs(start, current, cost, visited, depth):
    global min_cost
    
    visited[current] = True
    if depth == N and arr[current][start] != 0:
        cost += arr[current][start]
        min_cost = min(cost, min_cost)
        return min_cost
    
    for next in range(N):
        if not visited[next] and arr[current][next] != 0:
            visited[next] = True
            dfs(start, next, cost + arr[current][next], visited, depth + 1)
            visited[next] = False

visited = [False] * N
dfs(0, 0, 0, visited, 1)
print(min_cost)
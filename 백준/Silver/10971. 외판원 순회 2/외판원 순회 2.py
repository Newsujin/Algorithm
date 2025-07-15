N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')

def dfs(start, current, visited, cost, depth):
    global min_cost
    if depth == N and cities[current][start] != 0:
        cost += cities[current][start]
        min_cost = min(min_cost, cost)
        return
    
    for next_city in range(N):
        if not visited[next_city] and cities[current][next_city] != 0:
            visited[next_city] = True
            dfs(start, next_city, visited, cost + cities[current][next_city], depth + 1)
            visited[next_city] = False
    
for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(i, i, visited, 0, 1)

print(min_cost)
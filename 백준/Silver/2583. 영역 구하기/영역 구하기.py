import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, sys.stdin.readline().split())
rectangles = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
graph = [[False] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fill_rectangles():
    for rectangle in rectangles:
        for i in range(rectangle[1], rectangle[3]):
            for j in range(rectangle[0], rectangle[2]):
                graph[i][j] = True

def dfs(x, y, area):
    visited[y][x] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx] and not graph[ny][nx]:
            visited[ny][nx] = True
            area = dfs(nx, ny, area + 1)
    return area

fill_rectangles()
empty_area = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            empty_area.append(dfs(j, i, 1))

empty_area.sort()
print(len(empty_area))
for area in empty_area:
    print(area, end=' ')
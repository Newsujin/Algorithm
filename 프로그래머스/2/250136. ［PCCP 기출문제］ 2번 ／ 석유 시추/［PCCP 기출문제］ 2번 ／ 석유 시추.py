from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(land, x, y, oil_sum_by_row):
    q = deque([(x, y)])
    oil_area = 0
    visited[y][x] = True
    visited_col = set()
    visited_col.add(x)
    while q:
        oil_area += 1
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(land[0]) and 0 <= ny < len(land) and land[ny][nx] == 1 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                visited_col.add(nx)
    for col in visited_col:
        oil_sum_by_row[col] += oil_area

def solution(land):
    global visited
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    oil_sum_by_row = [0 for _ in range(len(land[0]))]
    for x in range(len(land[0])):
        for y in range(len(land)):
            if land[y][x] == 1 and not visited[y][x]:
                bfs(land, x, y, oil_sum_by_row)
    return max(oil_sum_by_row)
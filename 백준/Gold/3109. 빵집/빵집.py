import sys

r, c = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

directions = [(-1, 1), (0, 1), (1, 1)]

def dfs(row, col):
    maps[row][col] = 'x'
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < r and 0 <= nc < c and maps[nr][nc] == '.':
            if nc == c - 1:
                return True
            if dfs(nr, nc):
                return True
    return False

max_pipelines = 0
for row in range(r):
    if dfs(row, 0):
        max_pipelines += 1

print(max_pipelines)
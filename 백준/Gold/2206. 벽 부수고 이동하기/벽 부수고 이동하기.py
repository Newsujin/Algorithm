import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        x, y, b = q.popleft()
        if x == m - 1 and y == n - 1:
            return visited[y][x][b]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not maps[ny][nx] and not visited[ny][nx][b]:
                    visited[ny][nx][b] = visited[y][x][b] + 1
                    q.append((nx, ny, b))
                elif maps[ny][nx] and not b:
                    visited[ny][nx][b + 1] = visited[y][x][b] + 1
                    q.append((nx, ny, b + 1))
    return -1

print(bfs())
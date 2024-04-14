import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
s_y, s_x, s_d = map(lambda x: int(x) - 1, input().split())
t_y, t_x, t_d = map(lambda x: int(x) - 1, input().split())
visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
rotate = {0:[2, 3], 1:[2, 3], 2:[0, 1], 3:[0, 1]}

def bfs(x, y, d):
    visited[y][x][d] = 1
    q = deque([(x, y, d, 0)])

    while q:
        x, y, d, cnt = q.popleft()
        if (x, y, d) == (t_x, t_y, t_d):
            return cnt
        for step in range(1, 4):
            nx, ny = x + dx[d] * step, y + dy[d] * step
            if 0 > ny or ny >= M or 0 > nx or nx >= N or graph[ny][nx]: break
            if not visited[ny][nx][d]:
                visited[ny][nx][d] = 1
                q.append((nx, ny, d, cnt + 1))
        for r_d in rotate[d]:
            if not visited[y][x][r_d]:
                visited[y][x][r_d] = 1
                q.append((x, y, r_d, cnt + 1))

    return -1

print(bfs(s_x, s_y, s_d))
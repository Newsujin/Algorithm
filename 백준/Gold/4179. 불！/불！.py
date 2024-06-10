import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
jihoon = deque()
fire = deque()

f_time = [[0] * C for _ in range(R)]
j_time = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jihoon.append([i, j])
            j_time[i][j] = 1
        if maze[i][j] == 'F':
            fire.append([i, j])
            f_time[i][j] = 1


def bfs():
    while fire:
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
            if maze[nx][ny] != '#' and not f_time[nx][ny]:
                f_time[nx][ny] = f_time[x][y] + 1
                fire.append([nx, ny])
        
    while jihoon:
        x, y = jihoon.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return j_time[x][y]
            if maze[nx][ny] == '#' or j_time[nx][ny]: continue
            if not f_time[nx][ny] or f_time[nx][ny] > j_time[x][y] + 1:
                j_time[nx][ny] = j_time[x][y] + 1
                jihoon.append([nx, ny])
    return "IMPOSSIBLE"


print(bfs())
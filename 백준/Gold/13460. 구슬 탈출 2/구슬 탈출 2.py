import sys
from collections import deque

def get_pos():
    global rx, ry, bx, by
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = j, i
            elif board[i][j] == 'B':
                bx, by = j, i


def move(x, y, i, j):
    cnt = 0
    while board[y + j][x + i] != '#' and board[y][x] != 'O':
        x += i
        y += j
        cnt += 1
    return x, y, cnt


def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10:
            break

        for i in range(4):
            nrx, nry, r_cnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_cnt = move(bx, by, dx[i], dy[i])
            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                return cnt
            if nrx == nbx and nry == nby:
                if r_cnt > b_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))
    
    return -1


n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
get_pos()
q = deque([(rx, ry, bx, by, 1)])
visited = [(rx, ry, bx, by)]


print(bfs())
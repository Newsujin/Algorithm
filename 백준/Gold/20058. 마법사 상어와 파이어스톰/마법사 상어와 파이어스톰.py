import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
len_board = 2 ** N
board = [list(map(int, sys.stdin.readline().split())) for _ in range(2 ** N)]
L_list = list(map(int, sys.stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate_and_melting(board, len_board, L):
    new_board = [[0] * len_board for _ in range(len_board)]

    # rotate
    r_size = 2 ** L
    for y in range(0, len_board, r_size):
        for x in range(0, len_board, r_size):
            for i in range(r_size):
                for j in range(r_size):
                    new_board[y + j][x + r_size - i - 1] = board[y + i][x + j]

    board = new_board
    melting_list = []
    for y in range(len_board):
        for x in range(len_board):
            ice_count = 0
            for d in range(len(dy)):
                ny = y + dy[d]
                nx = x + dx[d]

                if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board:
                    continue
                elif board[ny][nx] > 0:
                    ice_count += 1

            if ice_count < 3 and board[y][x] != 0:
                melting_list.append((y, x))

    # 저장된 얼음들을 녹임
    for y, x in melting_list:
        board[y][x] -= 1

    return board

def check_ice_bfs(board, len_board):
    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            # BFS를 이용하여 얼음 덩어리 조사
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx]
                area_count += 1

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count)

    print(ice_sum)
    print(max_area_count)

for L in L_list:
        board = rotate_and_melting(board, len_board, L)

check_ice_bfs(board, len_board)

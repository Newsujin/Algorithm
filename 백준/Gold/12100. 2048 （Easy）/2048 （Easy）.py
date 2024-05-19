import sys
from copy import deepcopy


n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0


def move_left(board):
    for i in range(n):
        cursor = 0
        for j in range(n):

            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if not board[i][cursor]:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[i][cursor] = tmp
    
    return board


def move_right(board):
    for i in range(n):
        cursor = n - 1
        for j in range(n - 1, -1, -1):

            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if not board[i][cursor]:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp

    return board


def move_up(board):
    for j in range(n):
        cursor = 0
        for i in range(n):

            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if not board[cursor][j]:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = tmp
                    
    return board


def move_down(board):
    for j in range(n):
        cursor = n - 1
        for i in range(n - 1, -1, -1):

            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if not board[cursor][j]:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
                    
    return board


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return
    
    for i in range(4):
        tmp_board = deepcopy(board)
        if i == 0:
            dfs(move_left(tmp_board), cnt + 1)
        elif i == 1:
            dfs(move_right(tmp_board), cnt + 1)
        elif i == 2:
            dfs(move_up(tmp_board), cnt + 1)
        else:
            dfs(move_down(tmp_board), cnt + 1)


dfs(board, 0)
print(ans)
import sys

board = []
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

max_value = -1
row, col = 0, 0
for i in range(9):
    for j in range(9):
        if board[i][j] > max_value:
            max_value = board[i][j]
            row, col = i, j

print(max_value)
print(row + 1, col + 1)
import sys

n = int(input())
board = [[False for _ in range(100)] for _ in range(100)] 
extent = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for j in range(y, y + 10):
        for i in range(x, x + 10):
            if board[j][i] == 0:
                board[j][i] = 1
                extent += 1

print(extent)
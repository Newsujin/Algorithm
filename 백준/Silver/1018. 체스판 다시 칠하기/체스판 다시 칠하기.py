import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = list(input() for _ in range(N))

min_cnt = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        w_cnt = 0
        b_cnt = 0
        
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        w_cnt += 1
                    if board[x][y] != 'B':
                        b_cnt += 1
                else:
                    if board[x][y] != 'B':
                        w_cnt += 1
                    if board[x][y] != 'W':
                        b_cnt += 1

        min_cnt = min(min_cnt, w_cnt, b_cnt)

print(min_cnt)
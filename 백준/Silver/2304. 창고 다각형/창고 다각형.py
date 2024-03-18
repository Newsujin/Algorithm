import sys

n = int(sys.stdin.readline())
sticks = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sticks.sort()

tall_idx = 0
tall = 0
# 가장 높은 기둥 찾기
for i in range(n):
    if (sticks[i][1] > tall):
        tall = sticks[i][1]
        tall_idx = i
area = tall

# 가장 높은 기둥 왼쪽 면적 구하기
cur_x, cur_y = sticks[0][0], sticks[0][1]
for i in range(tall_idx):
    if cur_y <= sticks[i + 1][1]:
        area +=  cur_y * (sticks[i + 1][0] - cur_x)
        cur_x = sticks[i + 1][0]
        cur_y = sticks[i + 1][1]

# 가장 높은 기둥 왼쪽 면적 구하기
cur_x, cur_y = sticks[n - 1][0], sticks[n - 1][1]
for i in range(n - 1, tall_idx, -1):
    if cur_y <= sticks[i - 1][1]:
        area +=  cur_y * (cur_x - sticks[i - 1][0])
        cur_x = sticks[i - 1][0]
        cur_y = sticks[i - 1][1]

print(area)
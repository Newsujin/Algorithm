import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
map = list(list(sys.stdin.readline().strip()) for _ in range(r))
visited = [[0] * c for _ in range(r)]
hedgehog_q, water_q = deque(), deque()
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 물과 고슴도치 위치를 큐에 추가
for i in range(r):
    for j in range(c):
        if map[i][j] == '*':
            water_q.append((j, i))
        elif map[i][j] == 'S':
            visited[i][j] = 1
            hedgehog_q.append((j, i))

# 물과 고슴도치의 동시 이동을 위해 hedgehog_q 존재할 동안 반복
while hedgehog_q:
    cnt += 1
    # 물 확장
    cur = len(water_q)
    for _ in range(cur):
        x, y = water_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and map[ny][nx] == '.':
                water_q.append((nx, ny))
                map[ny][nx] = '*'
    # 고슴도치 이동
    cur = len(hedgehog_q)
    for _ in range(cur):
        x, y = hedgehog_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx] and (map[ny][nx] == '.' or map[ny][nx] == 'D'):
                if map[ny][nx] == 'D':
                    print(cnt)
                    exit()
                hedgehog_q.append((nx, ny))
                visited[ny][nx] = 1

print("KAKTUS")
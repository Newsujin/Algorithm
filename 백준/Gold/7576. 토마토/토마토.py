from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range (n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ripe_tomato = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            ripe_tomato.append((i, j))

day = -1
while ripe_tomato:
    for _ in range(len(ripe_tomato)):
        x, y = ripe_tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = 1
                ripe_tomato.append((nx, ny))
    day += 1

if all(all(cell != 0 for cell in row) for row in box):
    print(day)
else:
    print(-1)
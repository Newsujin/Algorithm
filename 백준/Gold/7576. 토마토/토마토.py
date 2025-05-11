from collections import deque

m, n = map(int, input().split())
box = []
q = deque()
for i in range(n):
    row = list(map(int, input().split()))
    box.append(row)
    for j in range(m):
        if row[j] == 1:
            q.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))

bfs()
res = 0
for row in box:
    if 0 in row:
        res = -1
        break
    res = max(res, max(row))

print(res - 1 if res != -1 else -1)
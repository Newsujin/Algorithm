from collections import deque

def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1):
                maps[nx][ny] = maps[x][y] + 1
                if (nx == len(maps) - 1 and ny == len(maps[0]) - 1):
                    return maps[nx][ny]
                q.append((nx, ny))

    return -1
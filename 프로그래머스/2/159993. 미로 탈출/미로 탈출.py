from collections import deque

def bfs(start, end, maps):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    flag = False
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i, j, 0))
                visited[i][j] = True
                flag = True
                break
        if flag: break
        
    while q:
        y, x, dist = q.popleft()
        if maps[y][x] == end:
            return dist

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and maps[ny][nx] != 'X':
                q.append((ny, nx, dist + 1))
                visited[ny][nx] = True
    
    return -1


def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    
    if path1 != -1 and path2 != -1:
        return path1 + path2
    
    return -1
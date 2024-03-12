import sys
from collections import deque

horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start_x, start_y, K):
    q = deque([(start_x, start_y, 0, 0)])
    visited = set([(start_x, start_y, 0)])
    
    while q:
        x, y, total_moves, horse_moves = q.popleft()
        if x == target_x and y == target_y:
            return total_moves
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < W and 0 <= ny < H and board[ny][nx] == 0 and (nx, ny, horse_moves) not in visited:
                visited.add((nx, ny, horse_moves))
                q.append((nx, ny, total_moves + 1, horse_moves))
        
        if horse_moves < K:
            for i in range(8):
                nx, ny = x + horse_dx[i], y + horse_dy[i]
                if 0 <= nx < W and 0 <= ny < H and board[ny][nx] == 0 and (nx, ny, horse_moves + 1) not in visited:
                    visited.add((nx, ny, horse_moves + 1))
                    q.append((nx, ny, total_moves + 1, horse_moves + 1))
                    
    return -1

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
start_x, start_y = 0, 0
target_x, target_y = W - 1, H - 1
print(bfs(start_x, start_y, K))
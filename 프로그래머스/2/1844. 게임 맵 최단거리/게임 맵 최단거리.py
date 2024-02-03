from collections import deque

def solution(maps):
	answer = 0
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	queue = deque()
	queue.append((0, 0))
		
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			h = len(maps)
			w = len(maps[0])
			if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
				maps[nx][ny] = maps[x][y] + 1
				queue.append((nx, ny))
	answer = maps[h - 1][w -1]
	return answer if answer != 1 else -1
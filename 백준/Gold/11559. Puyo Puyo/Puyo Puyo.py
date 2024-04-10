import sys
from collections import deque

graph = [list(sys.stdin.readline().strip()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_connected_puyo(y, x):
	visited = [[False for _ in range(6)] for _ in range(12)]
	q  = deque([(x, y)])
	connected_puyo = set()
	connected_puyo.add((x, y))

	while q:
		x, y = q.popleft()
		visited[y][x] = True
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < 6 and 0 <= ny < 12 and not visited[ny][nx] and graph[y][x] == graph[ny][nx]:
				visited[ny][nx] = True
				q.append((nx, ny))
				connected_puyo.add((nx, ny))

	if len(connected_puyo) >= 4:
		return connected_puyo
	return False


def pop_puyo(puyos):
	for x, y in puyos:
		graph[y][x] = '.'


def gravity():
	for j in range(6):
		stack = []
		for i in range(11, -1, -1):
			if graph[i][j] != '.':
				stack.append((graph[i][j]))
		for i in range(11, -1, -1):
			if stack:
				graph[i][j] = stack.pop(0)
			else:
				graph[i][j] = '.'


pop_cnt = 0
while True:
	chain = False
	for i in range(12):
		for j in range(6):
			if graph[i][j] != '.':
				puyos = find_connected_puyo(i, j)
				if puyos:
					pop_puyo(puyos)
					chain = True
	if not chain:
		break
	gravity()
	pop_cnt += 1


print(pop_cnt)
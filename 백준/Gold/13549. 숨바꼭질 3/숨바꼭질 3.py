import sys
from collections import deque

def bfs(v):
	q = deque([v])
	while q:
		v = q.popleft()
		if v == K:
			return visited[v]
		for next_v in [v - 1, v + 1, v * 2]:
			if 0 <= next_v < max_input and not visited[next_v]:
				if next_v == v * 2 and next_v != 0:
					visited[next_v] = visited[v]
					q.appendleft(next_v)
				else:
					visited[next_v] = visited[v] + 1
					q.append(next_v)

N, K = map(int, sys.stdin.readline().split())
max_input = 100001
visited = [0] * max_input
print(bfs(N))

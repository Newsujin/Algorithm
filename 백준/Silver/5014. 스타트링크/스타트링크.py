from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)]

def bfs():
	q = deque([S])
	visited[S] = 1
	while q:
		cur = q.popleft()
		if cur == G:
			return visited[cur] - 1
		for d in (cur + U, cur - D):
			if (0 < d <= F) and not visited[d]:
				visited[d] = visited[cur] + 1
				q.append(d)
	return ("use the stairs")

print (bfs())
import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
relation = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
connected = False
for _ in range(m):
	x, y = map(int, sys.stdin.readline().split())
	relation[x].append(y)
	relation[y].append(x)

def dfs(a, num):
	global connected
	visited[a] = True
	if a == b:
		connected = True
		return (print(num))
	for person in relation[a]:
		if not visited[person]:
			dfs(person, num + 1)

dfs(a, 0)
if not connected:
	print (-1)
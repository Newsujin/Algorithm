import sys

n = int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
	arr[int(sys.stdin.readline())].append(i)


def dfs(v, i):
	visited[v] = 1

	for k in arr[v]:
		if not visited[k]:
			dfs(k, i)
		elif k == i:
			res.append(k)


res = []
for i in range(1, n + 1):
	visited = [0] * (n + 1)
	dfs(i, i)


print(len(res))
[print(i) for i in res]
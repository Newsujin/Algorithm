import sys, math

def mst():
	total = 0
	now = 0

	for i in range(n):
		min = math.inf
		flag = False
		for pre in range(n):
			if now != pre and not visited[pre] and D[pre] < min:
				min = D[pre]
				now = pre
				flag = True

		if not i or flag:
			visited[now] = 1
			if i:
				total += min
		else:
			print(-1)
			return

		for pre in range(n):
			if not visited[pre]:
				tmp = (fields[now][0] - fields[pre][0]) ** 2 + (fields[now][1] - fields[pre][1]) ** 2
				if c <= tmp < D[pre]:
					D[pre] = tmp

	print(total)


n, c = map(int, sys.stdin.readline().split())
visited = [False] * n
D = [math.inf] * n
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mst()
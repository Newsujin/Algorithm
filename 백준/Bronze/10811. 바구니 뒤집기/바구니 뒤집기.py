import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(i for i in range(1, n + 1))

for _ in range(m):
	i, j = map(int, sys.stdin.readline().split())
	for x in range((j - i + 1) // 2):
		t =	arr[i - 1 + x]
		arr[i - 1 + x] = arr[j - 1 - x]
		arr[j - 1 - x] = t

print(*arr)
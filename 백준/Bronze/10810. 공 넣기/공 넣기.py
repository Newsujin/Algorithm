import sys

n, m =  map(int, sys.stdin.readline().split())
bucket_list = [0] * n
for _ in range(m):
	i, j, k = map(int, sys.stdin.readline().split())
	for n in range(i - 1, j):
		bucket_list[n] = k
print(*bucket_list)
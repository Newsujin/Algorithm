import sys

n, m =  map(int, sys.stdin.readline().split())
bucket_list = [0] * n
for i in range(n):
	bucket_list[i] = i + 1
for _ in range(m):
	i, j = map(int, sys.stdin.readline().split())
	t = bucket_list[i - 1]
	bucket_list[i - 1] = bucket_list[j - 1]
	bucket_list[j - 1] = t
print(*bucket_list)
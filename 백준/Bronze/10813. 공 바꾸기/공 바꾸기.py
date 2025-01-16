import sys

n, m =  map(int, sys.stdin.readline().split())
bucket_list = [k + 1 for k in range(n)]
for _ in range(m):
	i, j = map(int, sys.stdin.readline().split())
	bucket_list[i - 1], bucket_list[j - 1] = bucket_list[j - 1], bucket_list[i - 1]
print(*bucket_list)
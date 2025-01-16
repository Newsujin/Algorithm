import sys

arr = [int(sys.stdin.readline()) for _ in range(10)]
for i in range(10):
	arr[i] = arr[i] % 42
res = set(arr)
print(len(res))
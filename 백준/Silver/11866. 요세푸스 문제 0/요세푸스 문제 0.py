n, k = map(int, input().split())
arr = list(range(1, n + 1))

idx = 0
res = []
while arr:
	idx = (idx + k - 1) % len(arr)
	res.append(arr[idx])
	arr.remove(arr[idx])

print('<', end='')
for i in range(len(res)):
	if i != len(res) - 1:
		print(res[i], end=', ')
	else:
		print(res[i], end='>')
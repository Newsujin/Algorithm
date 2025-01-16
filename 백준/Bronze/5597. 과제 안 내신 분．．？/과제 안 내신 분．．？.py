import sys

arr = [int(sys.stdin.readline()) for _ in range(28)]
arr.sort()
cnt = 0
for i in range(1, 31):
	if cnt == 2:
		break
	if i not in arr:
		print (i)
		cnt += 1
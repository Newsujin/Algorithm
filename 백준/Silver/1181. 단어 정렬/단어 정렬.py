import sys

n = int(sys.stdin.readline())
str = list(set(sys.stdin.readline().strip() for _ in range(n)))
str = sorted(str, key=lambda x:(len(x), x))
for c in str:
	print(c)
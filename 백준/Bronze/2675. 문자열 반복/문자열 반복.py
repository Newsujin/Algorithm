import sys

T = int(input())

for _ in range(T):
	R, S = sys.stdin.readline().split()
	for c in S:
		print(int(R) * c, end='')
	print()
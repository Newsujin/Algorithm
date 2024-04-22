import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi_belt = [int(sys.stdin.readline().strip()) for _ in range(n)]

max_num = 0
for i in range(n):
    if i + k >= n:
        num = set(sushi_belt[i:] + sushi_belt[:(i + k) % n] + [c])
    else:
        num = set(sushi_belt[i:i + k] + [c])
    max_num = max(max_num, len(num))

print(max_num)
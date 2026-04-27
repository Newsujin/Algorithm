N = int(input())
min_s = 1001

for _ in range(N):
    A, B = map(int, input().split())
    if A <= B:
        min_s = min(min_s, B)

if min_s == 1001:
    print(-1)
else:
    print(min_s)
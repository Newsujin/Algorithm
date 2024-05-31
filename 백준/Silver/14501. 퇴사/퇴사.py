import sys

n = int(sys.stdin.readline())
book = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n):
    T, P = book[i]
    if i + 1 <= n:
        dp[i + 1] = max(dp[i + 1], dp[i])
    if i + T <= n:
        dp[i + T] = max(dp[i + T], dp[i] + P)

print(max(dp))
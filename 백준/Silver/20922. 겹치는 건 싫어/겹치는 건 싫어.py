import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left = right = 0
cnt = [0] * (max(arr) + 1)
ans = 0

while right < N:
    if cnt[arr[right]] < K:
        cnt[arr[right]] += 1
        right += 1
    else:
        cnt[arr[left]] -= 1
        left += 1
    ans = max(ans, right - left)

print(ans)
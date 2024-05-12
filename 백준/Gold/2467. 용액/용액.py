import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
left, right = 0, n - 1
ans = [arr[left], arr[right]]

while right - 1 != left:
    tmp = arr[left] + arr[right]
    if tmp < 0:
        left += 1
    else:
        right -= 1
    if abs(sum(ans)) >= abs(arr[left] + arr[right]):
        ans = [arr[left], arr[right]]

print(ans[0], ans[1])
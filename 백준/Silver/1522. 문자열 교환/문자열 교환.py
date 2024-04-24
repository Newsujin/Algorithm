import sys

arr = sys.stdin.readline().rstrip()
a = arr.count('a')
arr += arr[0:a - 1]
ans = float('inf')

for i in range(len(arr) - a + 1):
    ans = min(ans, arr[i:i + a].count('b'))

print(ans)
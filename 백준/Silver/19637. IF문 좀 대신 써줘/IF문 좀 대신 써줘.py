import sys

n, m = map(int, input().split())
powers = [sys.stdin.readline().split() for _ in range(n)]
powers.sort(key=lambda x:int(x[1]))

nums = [int(sys.stdin.readline().strip()) for _ in range(m)]

for num in nums:
    right = len(powers) - 1
    left = 0
    result = None
    while left <= right:
        mid = (left + right) // 2
        if num <= int(powers[mid][1]):
            result = powers[mid][0]
            right = mid - 1
        else:
            left = mid + 1
    print(result)
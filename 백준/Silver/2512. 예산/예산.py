import sys

N = int(sys.stdin.readline())
cities = list(map(int, sys.stdin.readline().split()))
budgets = int(sys.stdin.readline())
start, end = 0, max(cities)

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in cities:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= budgets:
        start = mid + 1
    else:
        end = mid - 1

print(end)
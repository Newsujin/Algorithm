import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

start = 0
end = max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
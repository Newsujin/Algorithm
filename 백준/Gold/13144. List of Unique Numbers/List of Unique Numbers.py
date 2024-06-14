import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
answer = 0
visited = [False] * 100001

while start <= end and end < n:
    if not visited[arr[end]]:
        visited[arr[end]] = True
        end += 1
        answer += end - start
    else:
        visited[arr[start]] = False
        start += 1

print(answer)
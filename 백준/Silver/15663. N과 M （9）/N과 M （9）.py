import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))


def back():
    dup_check = 0
    if len(res) == M:
        print(*res)
        return
    
    for i in range(N):
        if dup_check != arr[i] and not visited[i]:
            res.append(arr[i])
            visited[i] = True
            dup_check = arr[i]
            back()
            res.pop()
            visited[i] = False


visited = [False] * N
res = []
back()
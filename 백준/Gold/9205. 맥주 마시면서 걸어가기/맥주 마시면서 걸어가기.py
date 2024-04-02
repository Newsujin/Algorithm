import sys
from collections import deque

def bfs():
    q = deque([(home[0], home[1])])
    while q:
        x, y = q.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            print("happy")
            return
        for i in range(len(store)):
            nx, ny = store[i]
            if abs(x - nx) + abs(y - ny) <= 1000 and not visited[i]:
                q.append((nx, ny))
                visited[i] = True
    print("sad")

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    home = list(map(int, sys.stdin.readline().split()))
    store = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    festival = list(map(int, sys.stdin.readline().split()))
    visited = [False for _ in range(n + 1)]
    bfs()
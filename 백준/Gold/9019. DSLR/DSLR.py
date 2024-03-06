import sys
from collections import deque

def bfs(start):
    q = deque([(start, "")])
    visited = [False] * 10000
    visited[start] = True
    
    while q:
        n, cmds = q.popleft()

        if n == B:
            return (cmds)
        
        # D
        next_n = (2 * n) % 10000
        if not visited[next_n]:
            visited[next_n] = True
            q.append((next_n, cmds + 'D'))
        
        # S
        next_n = n - 1 if n != 0 else 9999
        if not visited[next_n]:
            visited[next_n] = True
            q.append((next_n, cmds + 'S'))
        
        # L
        next_n = (n % 1000) * 10 + (n // 1000)
        if not visited[next_n]:
            visited[next_n] = True
            q.append((next_n, cmds + 'L'))
        
        # R
        next_n = (n % 10) * 1000 + (n // 10)
        if not visited[next_n]:
            visited[next_n] = True
            q.append((next_n, cmds + 'R'))
        
T = int(sys.stdin.readline().strip())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A))
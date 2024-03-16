import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
relation = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, sys.stdin.readline().split())
	relation[a].append(b)
	relation[b].append(a)

kevin_bacon_cnt = [float('inf') for _ in range(n + 1)]

def bfs(start, relation):
    global kevin_bacon_cnt
    kevin_bacon_cnt[start] = 0
    visited = [False for _ in range(n + 1)]
    q = deque([(start, 0)])
    visited[start] = True
    while (q):
        person, distance = q.popleft()
        kevin_bacon_cnt[start] += distance
        for friend in relation[person]:
             if not visited[friend]:
                  q.append((friend, distance + 1))
                  visited[friend] = True
    return kevin_bacon_cnt

for i in range(1, n + 1):
    bfs(i, relation)

print (kevin_bacon_cnt.index(min(kevin_bacon_cnt)))
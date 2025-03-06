from collections import deque
import sys

a, b = map(int, sys.stdin.readline().split())
q = deque([(a, 1)])

while q:
    now, cnt = q.popleft()
    if now > b:
        continue
    if now == b:
        print(cnt)
        break
    
    q.append((now * 2, cnt + 1))
    q.append((int(str(now) + '1'), cnt + 1))

else:
    print(-1)
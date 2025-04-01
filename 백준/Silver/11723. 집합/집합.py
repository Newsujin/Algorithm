import sys

input = sys.stdin.readline
M = int(input())
S = set()

for _ in range(M):
    tmp = input().rstrip()
    if tmp == 'all':
        S = set(range(1, 21))
        continue
    elif tmp == 'empty':
        S = set()
        continue

    cmd, n = tmp.split()
    if cmd == 'add':
        S.add(int(n))
    elif cmd == 'remove':
        S.discard(int(n))
    elif cmd == 'check':
        if int(n) in S:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if int(n) in S:
            S.discard(int(n))
        else:
            S.add(int(n))
import sys
from collections import deque

p, m = map(int, sys.stdin.readline().split())
players = []
for _ in range(p):
    l, n = sys.stdin.readline().split()
    players.append([int(l), n])

rooms = []
for lv, name in players:
    joined = False
    for room in rooms:
        if lv - 10 <= room[0] <= lv + 10 and len(room[1]) < m:
            joined = True
            room[1].append((lv, name))
            room[1].sort(key=lambda x:x[1])
            break
    if not joined:
        rooms.append([lv, [(lv, name)]])

for room in rooms:
    if len(room[1]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for lv, name in room[1]:
        print(lv, name)
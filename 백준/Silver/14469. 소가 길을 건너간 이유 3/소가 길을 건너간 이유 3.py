import sys

n = int(sys.stdin.readline())
cows = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cows.sort(key=lambda x:x[0])
time = 0

for i, cow in enumerate(cows):
    if i == 0:
        time = cow[0] + cow[1]
    else:
        if time > cow[0]:
            time += cow[1]
        else:
            time = cow[0] + cow[1]

print(time)
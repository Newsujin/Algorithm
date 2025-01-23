import sys

s = [sys.stdin.readline().strip() for _ in range(5)]

for i in range(15):
    for j in range(5):
        if len(s[j]) > i:
            print(s[j][i], end='')
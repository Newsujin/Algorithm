import sys

s = []
max_n = 0
for _ in range(5):
    row = sys.stdin.readline().strip()
    max_n = max(max_n, len(row))
    s.append(row)

res = ''
i = 0
while True:
    for j in range(5):
        if len(s[j]) > i:
            res += s[j][i]
    i += 1
    if i >= max_n:
        break

print(res)
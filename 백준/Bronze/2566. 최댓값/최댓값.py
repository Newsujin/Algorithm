import sys

max_list = []
for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    max_value = max(row)
    j = row.index(max_value)
    max_list.append([max_value, i, j])

val, r, c = max(max_list, key=lambda x:x[0])
print(val)
print(r + 1, c + 1)
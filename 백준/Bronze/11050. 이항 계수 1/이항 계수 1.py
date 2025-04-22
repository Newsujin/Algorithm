n, k = map(int, input().split())

son = 1
for i in range(n, 0, -1):
    son *= i
parent = 1
for i in range(k, 0, -1):
    parent *= i
for i in range(n - k, 0, -1):
    parent *= i

print(son // parent)
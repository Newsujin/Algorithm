import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    b = b % 4
    if b % 4 == 0:
        b = 4
    n = a ** b % 10
    if n == 0:
        print(10)
    else:
        print(n)
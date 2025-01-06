import sys

n = int(sys.stdin.readline())

cnt = n // 4 + (1 if n % 4 else 0)
for _ in range(cnt):
    print("long ", end="")

print("int")
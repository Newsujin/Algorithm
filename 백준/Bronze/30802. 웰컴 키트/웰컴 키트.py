import sys

input = sys.stdin.readline
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

T_cnt = 0
for size in sizes:
    T_cnt += size // T + (size % T != 0)
print(T_cnt)

print(sum(sizes) // P, sum(sizes) % P)
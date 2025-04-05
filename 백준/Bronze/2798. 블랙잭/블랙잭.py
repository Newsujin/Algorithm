from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in combinations(cards, 3):
    tmp_sum = sum(i)
    if tmp_sum <= M:
        max_sum = max(max_sum, sum(i))
print(max_sum)
import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card_dict = Counter(cards)

for num in nums:
    print(card_dict[num], end=' ')
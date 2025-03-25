import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cards.sort()

def binary_search(target, cards):
    start = 0
    end = len(cards) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if cards[mid] == target:
            return True
        elif cards[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


for num in nums:
    if binary_search(num, cards):
        print(1, end=' ')
    else:
        print(0, end=' ')
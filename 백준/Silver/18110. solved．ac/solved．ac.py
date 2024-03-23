import sys

def my_round(n):
    return int(n) + (1 if n - int(n) >= 0.5 else 0)

def solution():
    n = int(sys.stdin.readline())
    if n == 0:
        return print(0)
    difficulty = [int(sys.stdin.readline()) for _ in range(n)]
    difficulty.sort()

    num = my_round(n * 0.15)
    difficulty = difficulty[num:len(difficulty) - num]
    print(my_round(sum(difficulty) / len(difficulty)))

solution()
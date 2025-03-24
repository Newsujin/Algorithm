import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))


for i in B:
    if binary_search(i, A):
        print(1)
    else:
        print(0)
T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    res = 0
    min_n = float('inf')
    for n in arr:
        if n % 2 == 0:
            res += n
            min_n = min(min_n, n)
    print(res, min_n)
import sys

n, m = map(int, input().split())
memo = set(sys.stdin.readline().strip() for _ in range(n))
blog = [sys.stdin.readline().strip().split(',') for _ in range(m)]
for keywords in blog:
    for keyword in keywords:
        if keyword in memo:
            memo.remove(keyword)
    print(len(memo))
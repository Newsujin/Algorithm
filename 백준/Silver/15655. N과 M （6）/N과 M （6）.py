n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s = []

def back(x):
    if len(s) == m:
        print(*s)
        return
    for i in range(x, n):
        s.append(num[i])
        back(i + 1)
        s.pop()

back(0)
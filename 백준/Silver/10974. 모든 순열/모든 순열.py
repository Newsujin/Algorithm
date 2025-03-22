N = int(input())
S = []

def back(x):
    if len(S) == N:
        print(*S)
        return
    for i in range(1, N + 1):
        if i not in S:
            S.append(i)
            back(i)
            S.pop()

back(1)
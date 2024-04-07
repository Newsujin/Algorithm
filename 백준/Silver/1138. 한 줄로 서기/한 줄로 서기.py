n = int(input())
h = list(map(int, input().split()))
answer = [0] * n

for p in range(1, n + 1):
    t = h[p-1]
    cnt = 0
    for i in range(n):
        if cnt == t and answer[i] == 0:
            answer[i] = p
            break
        elif answer[i] == 0:
            cnt += 1
print(*answer)
N, K = map(int, input().split())
arr = [True for _ in range(N + 1)]

cnt = 0
for i in range(2, N + 1):
    if arr[i] == True:
        arr[i] = False
        cnt += 1
        if cnt == K:
            exit(print(i))
        j = 2
        while (i * j <= N):
            if arr[i * j] == True:
                arr[i * j] = False
                cnt += 1
                if cnt == K:
                    exit(print(i * j))
            j += 1
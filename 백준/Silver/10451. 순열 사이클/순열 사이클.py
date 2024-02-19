def dfs(i):
    visited[i] = True
    if not visited[permuutation[i]]:
        dfs(permuutation[i])

T = int(input())
for _ in range(T):
    N = int(input())
    permuutation = [0] + list(map(int ,input().split()))
    cycle_cnt = 0
    visited = [False] * (N + 1)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cycle_cnt += 1

    print(cycle_cnt)
def solution(k, dungeons):
    max_cnt = 0
    visited = [False] * len(dungeons)

    def dfs(k, cnt):
        nonlocal max_cnt
        max_cnt = max(max_cnt, cnt)

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], cnt + 1)
                visited[i] = False
    
    dfs(k, 0)
    return max_cnt
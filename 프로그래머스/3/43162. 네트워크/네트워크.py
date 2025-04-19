def dfs(computers, visited, start):
    visited[start] = True
    for i in range(len(computers)):
        if not visited[i] and computers[start][i]:
            dfs(computers, visited, i)


def solution(n, computers):
    visited = [False] * len(computers)
    network_cnt = 0
    
    for i in range(len(computers)):
        if not visited[i]:
            dfs(computers, visited, i)
            network_cnt += 1

    return network_cnt
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, visited):
        visited[node] = True
        cnt = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                cnt += dfs(neighbor, visited)
        return cnt
    
    answer = float('inf')
    for wire in wires:
        a, b = wire
        graph[a].remove(b)
        graph[b].remove(a)

        visited = [False] * (n + 1)
        connected_cnt1 = dfs(a, visited)
        connected_cnt2 = n - connected_cnt1

        diff = abs(connected_cnt1 - connected_cnt2)
        answer = min(answer, diff)

        graph[a].append(b)
        graph[b].append(a)
    
    return answer


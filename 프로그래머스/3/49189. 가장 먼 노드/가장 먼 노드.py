from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for val in edge:
        a, b = val
        graph[a].append(b)
        graph[b].append(a)

    distances = [0] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([(1, 0)])
    visited[1] = True

    while queue:
        node, distance = queue.popleft()
        distances[node] = distance
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, distance + 1))
    
    max_distance = max(distances)
    return distances.count(max_distance)
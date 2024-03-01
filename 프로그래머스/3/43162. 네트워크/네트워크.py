def dfs(visited, computers, node):
	visited[node] = True
	for neighbor in range(len(computers[node])):
		if not visited[neighbor] and computers[node][neighbor] == 1:
			dfs(visited, computers, neighbor)

def solution(n, computers):
	visited = [False] * n
	answer = 0
	for i in range(n):
		if not visited[i]:
			dfs(visited, computers, i)
			answer += 1
	return answer
def solution(numbers, target):
	cnt = 0
	def dfs(idx, current):
		nonlocal cnt
		if idx == len(numbers):
			if current == target:
				cnt += 1
			return
		dfs(idx + 1, current + numbers[idx])
		dfs(idx + 1, current - numbers[idx])
	dfs(0, 0)
	return cnt

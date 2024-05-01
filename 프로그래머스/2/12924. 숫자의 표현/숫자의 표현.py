def solution(n):
	cnt = 0
	start = 1
	end = 1
	n_sum = 1

	while end <= n:
		if n_sum == n:
			cnt += 1
			n_sum -= start
			start += 1
		elif n_sum < n:
			end += 1
			n_sum += end
		else:
			n_sum -= start
			start += 1
	return cnt
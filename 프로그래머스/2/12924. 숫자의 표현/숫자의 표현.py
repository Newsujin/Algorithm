def solution(n):
	cnt = 0
	for i in range(1, n + 1):
		tmp = 0
		for j in range(i, n + 1):
			tmp += j
			if tmp >= n:
				if tmp == n:
					cnt += 1
				break
	return cnt
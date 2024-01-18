def solution(citations):
	# citations.sort()
	m = 0
	for val in citations:
		cnt = 0
		for i in range(len(citations)):
			if val <= citations[i]:
				cnt += 1
		if val >= cnt:
			val = cnt
		if m < val:
			m = val
			# m = max(m, cnt)
	return m
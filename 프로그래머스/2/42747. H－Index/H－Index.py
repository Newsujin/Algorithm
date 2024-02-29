def solution(citations):
	m = 0
	for val in citations:
		cnt = 0
		for i in range(len(citations)):
			if val <= citations[i]:
				cnt += 1
		if val >= cnt:
			m = max(m, cnt)
	return m
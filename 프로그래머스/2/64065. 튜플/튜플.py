def solution(s):
	s = s[2:-2].split('},{')
	li = [n.split(',') for n in s]
	li.sort(key=len)

	answer = []
	for group in li:
		for n in group:
			if n not in answer:
				answer.append(n)

	return list(map(int, answer))
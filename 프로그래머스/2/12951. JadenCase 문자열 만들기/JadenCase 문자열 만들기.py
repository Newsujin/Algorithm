def solution(s):
	s = s.split(' ')
	for i, word in enumerate(s):
		s[i] = word.capitalize()
	return((' '.join(s)))
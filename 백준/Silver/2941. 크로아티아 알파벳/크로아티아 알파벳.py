croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for pattern in croatian:
	if pattern in s:
		n = s.count(pattern)
		s = s.replace(pattern, '*', n)
print(len(s))
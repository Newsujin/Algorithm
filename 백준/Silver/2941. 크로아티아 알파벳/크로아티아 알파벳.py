croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for pattern in croatian:
	s = s.replace(pattern, '*')
print(len(s))
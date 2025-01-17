s = input()
ans = []
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i, c in enumerate(alpha):
	idx = s.find(c)
	ans.append(idx)

print(*ans)
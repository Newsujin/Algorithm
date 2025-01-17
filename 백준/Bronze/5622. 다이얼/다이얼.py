s = input()
dic = {
	2: 'ABC', 3: 'DEF', 4: 'GHI',
	5: 'JKL', 6: 'MNO', 7: 'PQRS',
	8: 'TUV', 9: 'WXYZ'
}

ans = 0
for c in s:
	for key, value in dic.items():
		if c in value:
			ans += int(key) + 1

print(ans)
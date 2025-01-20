from collections import Counter

word = input()
word = word.upper()
counter = Counter(word)

top = counter.most_common(2)
if (len(top) > 1 and top[0][1] == top[1][1]):
	print('?')
else:
	print(top[0][0])
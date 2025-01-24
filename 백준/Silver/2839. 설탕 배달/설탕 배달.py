n = int(input())
tmp = n
bag = 0
max_five = n // 5

for i in range(max_five, -1, -1):
	bag = i
	tmp -= bag * 5
	if (tmp % 3):
		bag = -1
		tmp = n
	else:
		bag += tmp // 3
		break

print(bag)
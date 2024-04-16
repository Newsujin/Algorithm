def solution(picks, minerals):
	divided_minerals = [minerals[i:i + 5] for i in range(0, min(sum(picks) * 5, len(minerals)), 5)]

	fatigues = []
	for part in divided_minerals:
		fatigue = [0, 0, 0]
		for mineral in part:
			fatigue[0] += 1
			fatigue[1] += 5 if mineral == "diamond" else 1
			fatigue[2] += 25 if mineral == "diamond" else 5 if mineral == "iron" else 1
		fatigues.append(fatigue)

	fatigues.sort(key=lambda x:(-x[2], -x[1], -x[0]))

	ans = 0
	for part in fatigues:
		if picks[0]:
			ans += part[0]
			picks[0] -= 1
		elif picks[1]:
			ans += part[1]
			picks[1] -= 1
		elif picks[2]:
			ans += part[2]
			picks[2] -= 1
		else:
			break

	return ans
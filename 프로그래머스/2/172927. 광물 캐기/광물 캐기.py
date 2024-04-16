from collections import deque

def solution(picks, minerals):
	# 광물 5개씩 끊기
	divided_minerals = [minerals[i:i + 5] for i in range(0, min(sum(picks) * 5, len(minerals)), 5)]

	# 각 묶음에서 곡괭이 별로 필요한 피로도 계산
	fatigues = []
	for part in divided_minerals:
		fatigue = [0, 0, 0]
		for mineral in part:
			fatigue[0] += 1
			fatigue[1] += 5 if mineral == "diamond" else 1
			fatigue[2] += 25 if mineral == "diamond" else 5 if mineral == "iron" else 1
		fatigues.append(fatigue)
	print(fatigues)

	# 낮은 등급의 곡괭이 점수를 기준으로 내림차순 정렬
	fatigues.sort(key=lambda x:(-x[2], -x[1], x[0]))

	# 다이아몬드 곡괭이부터 순서대로 사용
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
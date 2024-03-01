def solution(distance, rocks, n):
	left = 0
	right = distance
	answer = 0
	rocks.append(distance)
	rocks.sort()

	while left <= right:
		mid = (left + right) // 2
		removed_rocks = 0
		pre_rock = 0
		for rock in rocks:
			if rock - pre_rock < mid:
				removed_rocks += 1
			else:
				pre_rock = rock

			if removed_rocks > n:
				break

		if removed_rocks > n:
			right = mid - 1
		else:
			answer = mid
			left = mid + 1

	return answer
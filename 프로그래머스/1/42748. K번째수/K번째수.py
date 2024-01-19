def solution(array, commands):
	answer = []
	for command in commands:
		piece = array[command[0] - 1:command[1]]
		piece.sort()
		answer.append(piece[command[2] - 1])
	return answer
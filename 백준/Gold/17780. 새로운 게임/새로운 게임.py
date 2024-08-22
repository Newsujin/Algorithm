import sys

n, k = map(int, sys.stdin.readline().split())
color = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
horse = [0 for _ in range(k)]

for i in range(k):
	r, c, d = map(int, sys.stdin.readline().split())
	horse[i] = [r - 1, c - 1, d - 1]
	chess[r - 1][c - 1].append(i)

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def move(horse_num):
	r, c, d = horse[horse_num]
	if horse_num != chess[r][c][0]:
		return 0

	nr = r + dr[d]
	nc = c + dc[d]

	# 파란색이거나 범위를 벗어나면 반대로 한 칸
	if not 0 <= nr < n or not 0 <= nc < n or color[nr][nc] == 2:
		if d == 0 or d == 1:
			new_d = (d + 1) % 2
		else:
			new_d = (d - 1) % 2 + 2
		horse[horse_num][2] = new_d
		nr = r + dr[new_d]
		nc = c + dc[new_d]
		# 반대 방향도 파란색이거나 범위를 벗어나면 이동하지 않음
		if not 0 <= nr < n or not 0 <= nc < n or color[nr][nc] == 2:
			return 0

	chess_set = []
	chess_set.extend(chess[r][c])
	chess[r][c] = []

	# 빨간색인 경우 순서 반대로
	if color[nr][nc] == 1:
		chess_set.reverse()

	for i in chess_set: 
		chess[nr][nc].append(i)
		horse[i][:2] = [nr, nc]

	# 말이 4개 이상일 경우 종료
	if len(chess[nr][nc]) >= 4:
		return 1
	return 0


turn = 1
while turn <= 1000:
	for i in range(k):
		if move(i):
			print(turn)
			sys.exit()
	turn += 1
print(-1)
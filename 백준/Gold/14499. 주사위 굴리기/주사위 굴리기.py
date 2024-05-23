import sys

# 입력 받기
n, m, y, x, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cmd = list(map(int, sys.stdin.readline().split()))

# 주사위 초기화
dice = [0] * 6
dr = [0, 0, 0, -1, 1]  # 동, 서, 북, 남
dc = [0, 1, -1, 0, 0]

# 명령어 순서대로 실행
for c in cmd:
    nx = x + dc[c]
    ny = y + dr[c]

    # 지도 벗어나면 continue
    if not (0 <= nx < m and 0 <= ny < n):
        continue

    # 주사위 굴리기
    if c == 1:  # 동
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif c == 2:  # 서
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif c == 3:  # 북
        dice[2], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[2]
    elif c == 4:  # 남
        dice[2], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[2], dice[3]

    # 지도와 주사위 상호작용
    if graph[ny][nx] == 0:
        graph[ny][nx] = dice[5]
    else:
        dice[5] = graph[ny][nx]
        graph[ny][nx] = 0

    x, y = nx, ny
    print(dice[4])

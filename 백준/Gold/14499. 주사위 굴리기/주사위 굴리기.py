import sys

n, m, y, x, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cmd = list(map(int, sys.stdin.readline().split()))

dice = [0] * 6
dr = [0, 0, 0, -1, 1] # 동서북남
dc = [0, 1, -1, 0, 0]


# 명령어 순서대로 실행
for c in cmd:
    nx = x + dc[c]
    ny = y + dr[c]

    # map 벗어나면 continue
    if not 0 <= nx < m or not 0 <= ny < n: continue
    # 동서남북상하 저장
    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    # 주사위 굴리기
    if c == 1:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif c == 2:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif c == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif c == 4:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north
    
    # 지도 위 수 == 0
    if graph[ny][nx] == 0:
        graph[ny][nx] = dice[5]
    else:
        dice[5] = graph[ny][nx]
        graph[ny][nx] = 0
    
    x, y = nx, ny
    print(dice[4])
n, m = map(int,input().split()) # 세로, 가로

x, y, d = map(int,input().split()) # 현재 위치, 방향

array = []
for _ in range(n):
    array.append(list(map(int,input().split()))) # 장소의 상태

visited = [[0] * m for _ in range(n)] # 방문했는지 체크할 list
visited[x][y] = 1 # 현재 위치 방문처리

# 북,동,남,서 방향변수
dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global d

    d -= 1
    if d == -1:
        d = 3

turn_time = 0
count = 1
while True:
    turn_left()     # 왼쪽으로 회전
    nx = x + dx[d]
    ny = y + dy[d]
    if array[nx][ny] == 0 and visited[nx][ny] == 0: # 앞칸이 벽이 아니고 방문하지 않았다면
        x = nx
        y = ny                    # 이동
        visited[nx][ny] = 1       # 방문처리
        turn_time = 0             # 회전횟수 초기화
        count += 1                # 칸 수 세어줌
    else: # 벽이거나 방문한 곳이라면
        turn_time += 1  # 회전횟수만 증가
    if turn_time == 4:  # 회전횟수가 4라면 
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 0: # 뒤칸이 벽이 아니라면
            x = nx
            y = ny             # 이동
            turn_time = 0      # 회전횟수 초기화
        else:                  # 벽이라면
            break              # 종료

print(count)

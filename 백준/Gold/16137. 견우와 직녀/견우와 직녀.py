import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_intersection(x, y):
    row_cnt = 0
    col_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            if i % 2 == 0:
                row_cnt += 1
            else:
                col_cnt += 1
    if row_cnt > 0 and col_cnt > 0:
        return True
    else:
        return False

def bfs():
    queue = []
    heapq.heappush(queue, (0, 0, 0, False))
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True
    while queue:
        t, x, y, step = heapq.heappop(queue)
        #step = x,y가 오작교인지 확인하는 flag변수 (step==True면 이번에는 오작교 건널 수 x)
        #isSet = 새로운 오작교를 하나 만든 상태인지 확인하는 flag변수
        visited[x][y] = True
        if x == N - 1 and y == N - 1:
            return t
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    heapq.heappush(queue, (t + 1, nx, ny, False))
                if step == True and graph[nx][ny] != 1: #0,-1,2,... 모든 오작교 후보들.
                    continue
                elif graph[nx][ny] > 1: #이미 만들어진 오작교
                        nextTime = (t // graph[nx][ny] + 1) * graph[nx][ny]
                        heapq.heappush(queue, (nextTime, nx, ny, True))
    return -1

result = 1e9
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            if not is_intersection(i, j): #가로 세로가 교차하는 절벽이 아님
                graph[i][j] = M
                tmp_result = bfs()
                if tmp_result != -1:
                    result = min(result, tmp_result)
                graph[i][j] = 0

print(result)
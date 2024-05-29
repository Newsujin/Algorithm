import sys, heapq


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra():
    q = []
    heapq.heappush(q, [cave[0][0], 0, 0])

    while q:
        coin_sum, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(f'Problem {test_cnt}: {cost[y][x]}')

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and cost[ny][nx] > cave[ny][nx] + coin_sum:
                cost[ny][nx] = cave[ny][nx] + coin_sum
                heapq.heappush(q, [cost[ny][nx], nx, ny])


test_cnt = 1
while (True):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    cost = [[int(10e9)] * n for _ in range(n)]

    dijkstra()
    test_cnt += 1
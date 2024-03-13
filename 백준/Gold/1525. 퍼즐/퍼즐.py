import sys
from collections import deque

table = ''.join(''.join(list(sys.stdin.readline().split())) for _ in range(3))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = {table: 0}

def bfs():
    global table
    q = deque([table])
    while q:
        table = q.popleft()
        cnt = visited[table]
        if table == '123456780':
            return cnt
        
        zero_idx = table.index('0')
        y = zero_idx // 3 # 2차원 배열의 행
        x = zero_idx % 3 # 2차원 배열의 열
        cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = ny * 3 + nx
                table_list = list(table) # 원소 swap을 위하여 list 전환
                table_list[zero_idx], table_list[nz] = table_list[nz], table_list[zero_idx]
                new_table = ''.join(table_list) # 딕셔너리를 위하여 문자열 전환
            
                if visited.get(new_table, 0) == 0:
                    visited[new_table] = cnt
                    q.append(new_table)

    return -1

print(bfs())
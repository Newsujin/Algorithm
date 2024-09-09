from itertools import combinations


def can_avoid_detection(board, teachers, n):
    for tx, ty in teachers:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = tx, ty
            while 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 'O':
                    break
                if board[nx][ny] == 'S':
                    return False
                nx += dx
                ny += dy
    return True


def solution(n, board):
    empty_spaces = []
    teachers = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                empty_spaces.append((i, j))
            elif board[i][j] == 'T':
                teachers.append((i, j))
    
    for obstacles in combinations(empty_spaces, 3):
        temp_board = [row[:] for row in board]
        for x, y in obstacles:
            temp_board[x][y] = 'O'
        
        if can_avoid_detection(temp_board, teachers, n):
            return "YES"
    
    return "NO"


n = int(input().strip())
board = [input().strip().split() for _ in range(n)]

print(solution(n, board))
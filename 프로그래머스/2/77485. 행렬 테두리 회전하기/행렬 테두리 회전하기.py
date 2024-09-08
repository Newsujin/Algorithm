def solution(rows, columns, queries):
    # 1. 행렬 초기화
    matrix = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]
    result = []
    
    # 2. 회전 수행
    for x1, y1, x2, y2 in queries:
        # 좌표를 0-based로 변환
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        # 회전 시작
        previous = matrix[x1][y1]
        minimum = previous

        # 상단 행 회전
        for y in range(y1 + 1, y2 + 1):
            matrix[x1][y], previous = previous, matrix[x1][y]
            minimum = min(minimum, previous)
        
        # 오른쪽 열 회전
        for x in range(x1 + 1, x2 + 1):
            matrix[x][y2], previous = previous, matrix[x][y2]
            minimum = min(minimum, previous)
        
        # 하단 행 회전
        for y in range(y2 - 1, y1 - 1, -1):
            matrix[x2][y], previous = previous, matrix[x2][y]
            minimum = min(minimum, previous)
        
        # 왼쪽 열 회전
        for x in range(x2 - 1, x1 - 1, -1):
            matrix[x][y1], previous = previous, matrix[x][y1]
            minimum = min(minimum, previous)
        
        # 현재 회전에서의 최소값 저장
        result.append(minimum)
    
    return result

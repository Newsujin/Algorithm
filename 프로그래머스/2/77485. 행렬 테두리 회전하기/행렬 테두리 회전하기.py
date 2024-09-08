def solution(rows, columns, queries):
    matrix = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)]
    result = []

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        prev = matrix[x1][y1]
        min_val = prev

        # 왼 -> 오 (위쪽 행)
        for y in range(y1 + 1, y2 + 1):
            tmp = matrix[x1][y]
            matrix[x1][y] = prev
            prev = tmp
            min_val = min(min_val, prev)

        # 위 -> 아래 (오른쪽 열)
        for x in range(x1 + 1, x2 + 1):
            tmp = matrix[x][y2]
            matrix[x][y2] = prev
            prev = tmp
            min_val = min(min_val, prev)

        # 오 -> 왼 (아래쪽 행)
        for y in range(y2 - 1, y1 - 1, -1):
            tmp = matrix[x2][y]
            matrix[x2][y] = prev
            prev = tmp
            min_val = min(min_val, prev)

        # 아래 -> 위 (왼쪽 열)
        for x in range(x2 - 1, x1 - 1, -1):
            tmp = matrix[x][y1]
            matrix[x][y1] = prev
            prev = tmp
            min_val = min(min_val, prev)

        result.append(min_val)

    return result

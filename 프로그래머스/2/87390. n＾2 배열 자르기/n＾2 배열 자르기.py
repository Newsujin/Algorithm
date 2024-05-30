def solution(n, left, right):
    arr = []
    for k in range(left, right + 1):
        row = k // n
        col = k % n
        arr.append(max(row, col) + 1)
    return arr
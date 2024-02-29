def solution(brown, yellow):
    wh = brown + yellow
    for h in range(1, wh + 1):
        if (wh / h) % 1 == 0:
            w = wh / h
            if w >= h and (2 * w + 2 * h - 4 == brown):
                return [w, h]

print(solution(10, 2))
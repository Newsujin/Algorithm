def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes:
        w = max(size)
        h = min(size)
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return max_w * max_h
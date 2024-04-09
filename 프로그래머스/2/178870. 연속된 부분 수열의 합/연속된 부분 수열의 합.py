from collections import deque

def solution(sequence, k):
    start = end = 0
    cur_sum = sequence[start]
    ans = [0, len(sequence)]

    while True:
        if cur_sum < k:
            end += 1
            if end == len(sequence):
                break
            cur_sum += sequence[end]
        else:
            if cur_sum == k:
                if end - start < ans[1] - ans[0]:
                    ans = [start, end]
            cur_sum -= sequence[start]
            start += 1
    return ans
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine).most_common()

    sum = 0
    cnt = 1
    for n in counter:
        sum += n[1]
        if sum >= k:
            break
        cnt += 1

    return cnt
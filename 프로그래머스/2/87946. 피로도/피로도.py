from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for permute in permutations(dungeons, len(dungeons)):
        cur_k = k
        cnt = 0
        for need_k, spend_k in permute:
            if cur_k >= need_k:
                cur_k -= spend_k
                cnt += 1
            if cnt > answer:
                answer = cnt
    return answer
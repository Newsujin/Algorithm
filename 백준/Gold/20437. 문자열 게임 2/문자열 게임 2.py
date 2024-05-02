import sys
from collections import defaultdict


def str_game():
    str_len = len(W)
    # 딕셔너리에 각 문자별 인덱스 저장
    alpha = defaultdict(list)
    for i in range(str_len):
        if W.count(W[i]) >= K:
            alpha[W[i]].append(i)

    # K개 이상의 문자가 없다면 -1
    if not alpha:
        return (-1,)
    
    # 문자열 게임 진행
    short = 10000
    long = 0
    for idx_list in alpha.values():
        for j in range(len(idx_list) - K + 1):
            cur_len = idx_list[K + j - 1] - idx_list[j] + 1
            if short > cur_len:
                short = cur_len
            if long < cur_len:
                long = cur_len
    
    return short, long


T = int(sys.stdin.readline())
for _ in range(T):
    W = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline())
    print(*str_game())
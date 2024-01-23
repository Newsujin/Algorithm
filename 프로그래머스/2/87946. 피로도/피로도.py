from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    dun_len = len(dungeons)
    
    for permute in permutations(dungeons, dun_len):
        hp = k
        cnt = 0
        for dg in permute:
            if hp >= dg[0]:
                hp -= dg[1]
                cnt += 1
            if cnt > answer:
                answer = cnt
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
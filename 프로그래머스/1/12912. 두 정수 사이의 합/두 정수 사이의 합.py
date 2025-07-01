def solution(a, b):
    answer = 0
    if a < b:
        min_v = a
        max_v = b
    else:
        min_v = b
        max_v = a
    
    for i in range(min_v, max_v + 1):
        answer += i

    return answer
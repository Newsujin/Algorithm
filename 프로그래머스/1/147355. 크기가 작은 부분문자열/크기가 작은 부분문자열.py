def solution(t, p):
    t_len = len(t)
    p_len = len(p)
    
    answer = 0
    for i in range(t_len - p_len + 1):
        if t[i:i + p_len] <= p:
            answer += 1
    
    return answer
def solution(s):
    answer = len(s)
    
    for unit in range(1, len(s) // 2 + 1):
        compressed = ''
        repeat_s = s[:unit]
        cnt = 1
        
        for i in range(unit, len(s), unit):
            if repeat_s == s[i:i + unit]:
                cnt += 1
            else:
                compressed += str(cnt) + repeat_s if cnt > 1 else repeat_s
                cnt = 1
                repeat_s = s[i:i + unit]
        
        compressed += str(cnt) + repeat_s if cnt > 1 else repeat_s
        answer = min(answer, len(compressed))
    
    return answer
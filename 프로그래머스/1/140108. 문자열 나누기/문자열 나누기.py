def solution(s):
    answer = 0
    isx, isnotx = 0, 0
    for i in range(len(s)):
        if isx == isnotx:
            answer += 1
            x = s[i]
            isx, isnotx = 0, 0
            
        if s[i] == x:
            isx += 1
        else:
            isnotx += 1
            
    return answer

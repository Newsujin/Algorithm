def solution(s):
    answer = ''
    s_len = len(s)
    if s_len == 1:
        return s
    if s_len % 2:
        answer = s[s_len // 2]
    else:
        answer = s[s_len // 2 - 1] + s[s_len // 2]
    return answer
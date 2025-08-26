def solution(s):
    s_len = len(s)
    if (s_len == 4 or s_len == 6) and s.isdigit():
        return True
    else:
        return False
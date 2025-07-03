def solution(phone_number):
    p_len = len(phone_number)
    answer = (p_len - 4) * '*' + phone_number[p_len - 4:]
    return answer
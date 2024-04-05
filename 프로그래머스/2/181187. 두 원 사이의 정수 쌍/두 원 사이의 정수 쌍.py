import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        y2 = math.floor(math.sqrt(r2**2 - x**2))
        y1 = y1 = 0 if x >= r1 else math.ceil(math.sqrt(r1**2 - x**2))
        answer += y2 - y1 + 1
    return answer * 4
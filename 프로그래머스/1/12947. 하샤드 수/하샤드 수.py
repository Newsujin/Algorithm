def solution(x):
    str_x = str(x)
    sum = 0
    for i in range(len(str_x)):
        sum += int(str_x[i])
    if x % sum == 0:
        return True
    return False
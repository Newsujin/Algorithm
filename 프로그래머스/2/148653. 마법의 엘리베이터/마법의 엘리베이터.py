def solution(storey):
    answer = 0
    while (storey > 0):
        n = storey % 10
        if (n > 5):
            answer += (10 - n)
            storey += (10 - n)
        elif (n < 5):
            answer += n
            storey -= n
        else:
            tmp = storey // 10
            if (tmp % 10 >= 5):
                answer += (10 - n)
                storey += (10 - n)
            else:
                answer += n
                storey -= n
        storey //= 10
    return answer
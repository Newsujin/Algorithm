def solution(n):
    i_list = []
    for i in range(1,n+1):
        if n%i == 1:
            i_list.append(i)
    answer = min(i_list)
    return answer
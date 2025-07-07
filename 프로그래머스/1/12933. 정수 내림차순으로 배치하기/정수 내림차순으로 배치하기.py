def solution(n):
    list_n = list(str(n))
    list_n.sort(reverse=True)

    return int(''.join(list_n))
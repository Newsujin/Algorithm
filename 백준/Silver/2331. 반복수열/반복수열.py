def solution(A, P):
    answer = [A]
    cur_n = A
    repeat_start_i = -1
    while repeat_start_i == -1:
        cur_n = sum(int(n) ** P for n in str(cur_n))
        if cur_n in answer:
            repeat_start_i = answer.index(cur_n)
        answer.append(cur_n)
    print(repeat_start_i)
    return (repeat_start_i)

A, P = map(int, input().split())
solution(A, P)
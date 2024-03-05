def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    for a in A:
        if a >= B[0]:
            continue
        else:
            del B[0]
            answer += 1
    return (answer)
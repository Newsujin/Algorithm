def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    tmp_lost = [i for i in lost if i not in reserve]
    tmp_reserve = [i for i in reserve if i not in lost]

    for i in tmp_reserve:
        if i - 1 in tmp_lost:
            tmp_lost.remove(i - 1)
        elif i + 1 in tmp_lost:
            tmp_lost.remove(i + 1)

    return n - len(tmp_lost)

print(solution(5, [2, 4], [1, 3, 5]))

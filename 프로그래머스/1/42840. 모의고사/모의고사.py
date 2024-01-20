def solution(answers):
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    cnt = [0, 0, 0]

    for i, val in enumerate(answers):
        if students[0][(i + 1) % 5 - 1] == val:
            cnt[0] += 1
        if students[1][(i + 1) % 8 - 1] == val:
            cnt[1] += 1
        if students[2][(i + 1) % 10 - 1] == val:
            cnt[2] += 1
    max_val = max(cnt)
    return [idx + 1 for idx, val in enumerate(cnt) if val == max_val]

print(solution([1,3,2,4,2]))
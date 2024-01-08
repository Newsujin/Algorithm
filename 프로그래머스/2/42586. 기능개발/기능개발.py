def solution(progresses, speeds):
    remaining_percent = []
    for i in range(len(progresses)):
        remaining_percent.append(((100 - progresses[i]) // speeds[i]) + ((100 - progresses[i]) % speeds[i] != 0))
    answer = []
    while remaining_percent:
        current_progress = remaining_percent.pop(0)
        cnt = 1
        while remaining_percent and current_progress >= remaining_percent[0]:
            remaining_percent.pop(0)
            cnt += 1
        answer.append(cnt)
    return answer
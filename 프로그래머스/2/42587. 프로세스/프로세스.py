from collections import deque

def solution(priorities, location):
    queue = deque()
    exec_cnt = 0

    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    while queue:
        current_value = queue.popleft()

        # 큐에 남아 있는 프로세스들과 비교
        for i in range(len(queue)):
            if current_value[0] < queue[i][0]:
                queue.append(current_value)
                break  # 우선순위가 더 높은 프로세스가 있으면 현재 프로세스를 큐에 넣고 중단
        else:
            exec_cnt += 1
            if current_value[1] == location:
                return exec_cnt

# 예제 실행
print(solution([2, 1, 3, 2], 3))

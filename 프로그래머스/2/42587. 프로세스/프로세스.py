from collections import deque

def solution(priorities, location):
    queue = deque()
    exec_cnt = 0
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    while queue:
        current_value = queue.popleft()
        for i in range(len(queue)):
            if (current_value[0] < queue[i][0]):
                    queue.append(current_value)
                    break
        else:
            exec_cnt += 1
            if current_value[1] == location:
                 return exec_cnt

print(solution([2, 1, 3, 2], 3))
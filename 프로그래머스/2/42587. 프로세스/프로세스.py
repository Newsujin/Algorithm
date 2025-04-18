from collections import deque

def solution(priorities, location):
    dq = deque()
    for i in range(len(priorities)):
        dq.append((i, priorities[i]))
    
    exec_cnt = 0
    while dq:
        cur_process = dq.popleft()
        for i in range(len(dq)):
            if cur_process[1] < dq[i][1]:
                dq.append(cur_process)
                break
        else:
            exec_cnt += 1
            if cur_process[0] == location:
                return exec_cnt
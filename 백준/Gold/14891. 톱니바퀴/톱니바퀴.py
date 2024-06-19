import sys
from collections import deque

input = sys.stdin.readline
wheels = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())
rotate_methods = [list(map(int, input().split())) for _ in range(K)]

def rotate(wheel, direction):
    if direction == 1:
        wheel.appendleft(wheel.pop())
    else:
        wheel.append(wheel.popleft())

for wheel_n, direction in rotate_methods:
    wheel_n -= 1
    rotations = [0] * 4
    rotations[wheel_n] = direction
    
    # 왼쪽으로 회전 전파
    for i in range(wheel_n, 0, -1):
        if wheels[i][6] != wheels[i - 1][2]:
            rotations[i - 1] = -rotations[i]
        else:
            break
    
    # 오른쪽으로 회전 전파
    for i in range(wheel_n, 3):
        if wheels[i][2] != wheels[i + 1][6]:
            rotations[i + 1] = -rotations[i]
        else:
            break
    
    # 회전 적용
    for i in range(4):
        if rotations[i] != 0:
            rotate(wheels[i], rotations[i])

# 점수 계산
score = sum((1 << i) if wheels[i][0] == 1 else 0 for i in range(4))
print(score)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    current_weight = 0

    while bridge:
        time += 1
        current_weight -= bridge.popleft()
        if truck_weights:
            if weight >= current_weight + truck_weights[0]:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
        else:
            bridge.append(0)
            if all(value == 0 for value in bridge):
                break
    return time

print(solution(2, 10, [7, 4, 5, 6]))
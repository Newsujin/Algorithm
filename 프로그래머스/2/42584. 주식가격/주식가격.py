def solution(prices):
    answer = []
    for idx in range(len(prices) - 1):
        for next_idx in range(idx + 1, len(prices)):
            if prices[next_idx] < prices[idx]:
                answer.append(next_idx - idx)
                break
        else:
            answer.append(len(prices) - idx - 1)
    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))
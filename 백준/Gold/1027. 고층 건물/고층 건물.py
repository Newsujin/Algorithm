import sys

input = sys.stdin.readline
N = int(input())
heights = list(map(int, input().split()))

answer = [0] * N

for i in range(N - 1):
    max_slope = -float('inf')
    for j in range(i + 1, N):
        slope = (heights[j] - heights[i]) / (j - i)
        # 현재 기울기가 최대 기울기보다 크다면, 빌딩 i에서 빌딩 j가 보인다.
        if slope > max_slope:
            max_slope = max(max_slope, slope)
            answer[i] += 1
            answer[j] += 1

print(max(answer))
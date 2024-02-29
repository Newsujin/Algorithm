import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if not scoville:  # 만약 한 개만 남아있는 경우
            return -1
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        cnt += 1
    return cnt
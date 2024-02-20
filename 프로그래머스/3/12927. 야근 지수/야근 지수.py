import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)

    for _ in range(n):
        if not works:
            break
        max_work = heapq.heappop(works)
        if max_work < 0:
            heapq.heappush(works, max_work + 1)
    
    answer = sum(work ** 2 for work in works)
    return answer
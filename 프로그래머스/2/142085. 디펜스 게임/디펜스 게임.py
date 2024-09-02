import heapq

def solution(n, k, enemy):
    max_heap = []
    for i, e in enumerate(enemy):
        if n >= e:
            heapq.heappush(max_heap, -e)
            n -= e
        else:
            if k > 0:
                if max_heap:
                    max_enemy = -heapq.heappop(max_heap)
                    if max_enemy > e:
                        n += max_enemy - e
                        heapq.heappush(max_heap, -e)
                    else:
                        heapq.heappush(max_heap, -max_enemy)
                k -= 1
            else:
                return i
    
    return len(enemy)
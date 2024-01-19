import heapq

def solution(operations):
	min_heap = []
	max_heap = []
	n = 0

	while operations:
		cmd, num = operations.pop(0).split()
		num = int(num)

		if cmd == 'I':
			heapq.heappush(min_heap, num)
			heapq.heappush(max_heap, -num)
		elif cmd == "D" and num == -1:
			if min_heap:
				min_val = heapq.heappop(min_heap)
				max_heap.remove(-min_val)
		elif cmd == "D" and num == 1:
			if max_heap:
				max_val = heapq.heappop(max_heap)
				min_heap.remove(-max_val)

	return [-max_heap[0], min_heap[0]] if max_heap and min_heap else [0, 0]
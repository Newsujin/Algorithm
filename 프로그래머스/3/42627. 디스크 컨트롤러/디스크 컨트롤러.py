import heapq

def solution(jobs):
	jobs.sort()
	answer = 0
	cur_time = 0
	heap = []
	len_jobs = len(jobs)

	while jobs or heap:
		while jobs and jobs[0][0] <= cur_time:
			start, duration = jobs.pop(0)
			heapq.heappush(heap, (duration, start))

		if heap:
			duration, start = heapq.heappop(heap)
			cur_time += duration
			answer += cur_time - start
		else:
			cur_time = jobs[0][0]

	return answer // len_jobs

print(solution([[0, 3], [1, 9], [2, 6]]))
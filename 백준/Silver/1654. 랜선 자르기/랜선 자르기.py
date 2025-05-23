import sys

K, N = map(int, sys.stdin.readline().strip().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(K)]
start, end = 1, max(lines)

while(start <= end):
  mid = (start + end) // 2
  line_cnt = 0

  for line in lines:
    line_cnt +=  line // mid
    
  if line_cnt >= N:
    start = mid + 1
  else:
    end = mid - 1

print(end)
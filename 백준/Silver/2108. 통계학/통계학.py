import sys
N = int(sys.stdin.readline())
arr=[]
sum_v = 0
for _ in range(N):
  x = int(sys.stdin.readline())
  arr.append(x)
  sum_v += x

arr.sort()

#산술평균
if sum_v <0:
  print(0 - abs(sum_v // N + (1 if (sum_v / N - sum_v // N) >= 0.5 else 0)))
else:
  print(sum_v // N + (1 if (sum_v / N - sum_v // N) >= 0.5 else 0))

#중앙값
print(arr[N // 2])

#최빈값
dict = {}
for a in arr:
  if a not in dict:
    dict[a] = 1
  else:
    dict[a] += 1
max_cnt = max(dict.values())
max_arr = sorted([k for k,v in dict.items() if v == max_cnt])
if len(max_arr) > 1:
  print(max_arr[1])
else:
  print(max_arr[0])

#범위
print(arr[-1] - arr[0])
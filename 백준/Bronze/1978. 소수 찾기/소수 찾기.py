import math

n = int(input())
nums = map(int, input().split())

cnt = 0
for num in nums:
    if num >= 2:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                break
        else:
            cnt += 1

print(cnt)
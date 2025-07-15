n = int(input())
arr = list(map(int, input().split()))
answer = [arr[0]]
for i in range(1, n):
    cur = arr[i] * (i + 1)
    for j in range(len(answer)):
        cur -= answer[j]    
    answer.append(cur)
print(*answer)
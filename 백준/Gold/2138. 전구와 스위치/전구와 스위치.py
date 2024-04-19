N = int(input())
cur = list(map(int, input()))
target = list(map(int, input()))

def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, N):
        
        if A_copy[i-1] == B[i-1]:
            continue
        
        press += 1
        for j in range(i-1, i+2):
            if j < N:
                A_copy[j] = 1 - A_copy[j]
    if A_copy == B:
        return press 
    else:
        return 1e9

# 첫 번째 전구의 스위치를 누르지 않은 경우
res = change(cur, target)
# 첫 번째 전구의 스위치를 누른 경우
cur[0] = 1 - cur[0]
cur[1] = 1 - cur[1]

res = min(res, change(cur, target) + 1)
print(res if res != 1e9 else -1) 
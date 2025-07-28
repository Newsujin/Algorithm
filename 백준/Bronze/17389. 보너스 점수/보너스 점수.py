N = int(input())
S = str(input())
answer = 0
bonus = 0

for i in range(len(S)):
    if S[i] == 'O':
        answer += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0 
        
print(answer)
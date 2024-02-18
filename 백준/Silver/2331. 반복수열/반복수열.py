A, P = map(int, input().split())
answer = [A]
cur_n = A
while True:
    cur_n = sum(int(n) ** P for n in str(cur_n))
    if cur_n in answer:
        break
    answer.append(cur_n)
print(answer.index(cur_n))
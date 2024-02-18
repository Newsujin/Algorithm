A, P = map(int, input().split())
answer = [A]
while True:
    cur_n = sum(int(n) ** P for n in str(answer[-1]))
    if cur_n in answer:
        break
    answer.append(cur_n)
print(answer.index(cur_n))
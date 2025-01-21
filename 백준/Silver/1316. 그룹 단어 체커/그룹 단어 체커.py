import sys

cnt = 0
for _ in range(int(input())):
    word = sys.stdin.readline()
    if len(word) == 1:
        cnt += 1
        continue

    res = [word[0]]
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            continue
        if word[i] in res:
            break
        res.append(word[i])
    else:
        cnt += 1

print(cnt)
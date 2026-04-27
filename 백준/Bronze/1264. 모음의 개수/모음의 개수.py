alpha = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    s = input()
    if s == '#':
        break
    cnt = 0
    for al in alpha:
        cnt += s.count(al)
    print(cnt)
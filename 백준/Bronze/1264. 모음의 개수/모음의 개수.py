while True:
    cnt=0
    n=input()
    if n == "#":
        break
    for i in n:
        if i in "aeiouAEIOU":
            cnt+=1
    print(cnt)
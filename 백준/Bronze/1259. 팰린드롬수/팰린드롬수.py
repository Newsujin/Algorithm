def drom(a):
    flag = 1
    for i in range(len(a) // 2):
        if a[i] != a[len(a) - 1 - i]:
            flag = 0
    return flag


a = input()

while a != "0":
    if drom(a):
        print("yes")
    else:
        print("no")
    a = input()
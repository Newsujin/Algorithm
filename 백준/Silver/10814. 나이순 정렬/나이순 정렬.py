import sys

input = sys.stdin.readline
n = int(input())
member = [list(input().split()) for _ in range(n)]
member.sort(key=lambda x:int(x[0]))
for age, name in member:
    print(age, name)
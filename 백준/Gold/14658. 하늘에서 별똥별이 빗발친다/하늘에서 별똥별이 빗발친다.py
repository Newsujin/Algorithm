import sys

input = sys.stdin.readline
n, m, l, k = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(k)]

max_stars = 0
for i in range(k):
    for j in range(k):
        tx = stars[i][0]
        ty = stars[j][1]

        cnt = 0
        for star in stars:
            if tx <= star[0] <= tx + l and ty <= star[1] <= ty + l:
                cnt += 1

        if cnt > max_stars:
            max_stars = cnt

print(k - max_stars)
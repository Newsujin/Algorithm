def paper(a, b, n):
    global white, blue
    color = field[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if color != field[i][j]:
                paper(a, b, n//2)
                paper(a + n//2, b, n//2)
                paper(a, b + n//2, n//2)
                paper(a + n//2, b + n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

global white, blue
white = 0
blue = 0
n = int(input())
field = [list(map(int,input().split())) for _ in range(n)]
paper(0, 0, n)
print(white)
print(blue)
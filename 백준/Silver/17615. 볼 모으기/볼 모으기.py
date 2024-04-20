import sys

N = int(sys.stdin.readline())
balls = str(sys.stdin.readline().rstrip())
cnt = []

# 우측으로 레드 모으기
rcollect = balls.rstrip('R')
cnt.append(rcollect.count('R'))

# 우측으로 블루 모으기
rcollect = balls.rstrip('B')
cnt.append(rcollect.count('B'))

# 좌측으로 레드 모으기
lcollect = balls.lstrip('R')
cnt.append(lcollect.count('R'))

# 좌측으로 블루 모으기
lcollect = balls.lstrip('B')
cnt.append(lcollect.count('B'))

print(min(cnt))

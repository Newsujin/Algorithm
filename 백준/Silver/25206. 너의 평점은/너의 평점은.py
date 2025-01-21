import sys

child = 0
parent = 0
grade_point = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0}

for _ in range(20):
    sub, score, grade = sys.stdin.readline().split()
    if grade == 'P':
        continue
    if grade != 'F':
        child += float(score) * grade_point[grade]
    parent += float(score)

print(child / parent)
import sys

stackA = list(sys.stdin.readline().strip())
stackB = []
M = int(sys.stdin.readline())
for _ in range(M):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "L" and stackA:
        stackB.append(stackA.pop())
    elif cmd[0] == "D" and stackB:
        stackA.append(stackB.pop())
    elif cmd[0] == "B" and stackA:
        stackA.pop()
    elif cmd[0] == "P":
        stackA.append(cmd[1])

stackA = stackA + stackB[::-1]
print("".join(stackA))
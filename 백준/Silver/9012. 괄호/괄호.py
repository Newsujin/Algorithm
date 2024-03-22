import sys

T = int(sys.stdin.readline())
for _ in range(T):
    arr = sys.stdin.readline().strip()
    stack = []

    is_vps = True
    for c in arr:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                is_vps = False
                break
            stack.pop()
            
    if not is_vps or stack:
        print("NO")
    else:
        print("YES")
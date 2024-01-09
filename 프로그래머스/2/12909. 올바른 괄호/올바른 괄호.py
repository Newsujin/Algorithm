def solution(s):
    stack = []
    for value in s:
        if value == '(':
            stack.append(value)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True
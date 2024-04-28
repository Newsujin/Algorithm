import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

def dfs(T):
	if S == T:
		return True
	if len(T) > 1 and T[-1] == 'A' and dfs(T[:-1]):
		return True
	if len(T) > 1 and T[0] == 'B' and dfs(T[1:][::-1]):
		return True
	return False

print(1 if dfs(T) else 0)
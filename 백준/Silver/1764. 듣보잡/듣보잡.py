import sys

n, m = map(int, sys.stdin.readline().split())
never_heard = list(sys.stdin.readline().rstrip() for _ in range(n))
never_seen = list(sys.stdin.readline().rstrip() for _ in range(m))
never_heard_seen = list(set(never_heard) & set(never_seen))

print(len(never_heard_seen))
for name in sorted(never_heard_seen):
    print(name)
N, M = map(int, input().split())
memo = dict()
for _ in range(N):
    site, pw = input().split()
    memo[site] = pw
target_sites = [input() for _ in range(M)]

for site in target_sites:
    print(memo[site])
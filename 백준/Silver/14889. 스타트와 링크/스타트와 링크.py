import sys
from itertools import combinations

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_dif = sys.maxsize
players = list(range(N))


def calculate_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score


for team1 in combinations(players, N // 2):
    team2 = list(set(players) - set(team1))
    
    score1 = calculate_score(team1)
    score2 = calculate_score(team2)
    min_dif = min(min_dif, abs(score1 - score2))

    if min_dif == 0:
        break


print(min_dif)
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    rank = list(map(int, sys.stdin.readline().split()))
    
    under_six = []
    for i in range(1, n + 1):
        if rank.count(i) < 6:
            under_six.append(i)
    rank = [team for team in rank if team not in under_six]
    
    score = {}
    for i, team in enumerate(rank):
        if team not in score:
            score[team] = [[i + 1], i + 1]
        else:
            score[team][0].append(i + 1)
            if len(score[team][0]) < 5:
                score[team][1] += i + 1

    answer = []
    for team, team_score in score.items():
        answer.append((team, team_score[0][4], team_score[1]))
    winner = sorted(answer, key=lambda x:(x[2], x[1]))
    
    print(winner[0][0])
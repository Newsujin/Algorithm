def solution(babbling):
    answer = 0
    
    li = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in li:
            if (j * 2 in i):
                break
            else:
                if (j in i):
                    i = i.replace(j, '0' * len(j))

        if (i.count('0') == len(i)):
            answer += 1

    return answer
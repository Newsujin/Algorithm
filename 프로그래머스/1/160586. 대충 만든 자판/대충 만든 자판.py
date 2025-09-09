def solution(keymap, targets):
    dic={}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            alphabet=keymap[i][j]
            if alphabet in dic.keys():
                dic[alphabet]=min(dic[alphabet], j+1)
            else:
                dic[alphabet]=j+1

    answer = []
    for i in range(len(targets)):
        total=0
        for j in range(len(targets[i])):
            if targets[i][j] in dic.keys():
                total+=dic[targets[i][j]]
            else:
                total=-1
                break
        answer.append(total)
    
    return answer
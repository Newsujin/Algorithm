def solution(players, callings):
    index_dic = {key: i for i, key in enumerate(players)}

    for pl in callings:
        index = index_dic[pl]
        index_dic[pl] -= 1
        index_dic[players[index-1]] += 1
        players[index-1], players[index] = players[index], players[index-1]

    return players
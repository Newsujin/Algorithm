def solution(clothes):
    sorted_clothes = {}
    for clo, category in clothes:
        if category in sorted_clothes.keys():
            sorted_clothes[category] += [clo]
        else:
            sorted_clothes[category] = [clo]
    
    answer = 1
    for _, value in sorted_clothes.items():
        answer *= (len(value) + 1)
    return answer - 1
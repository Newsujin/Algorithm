def solution(name, yearning, photo):
    result = []
    for p in photo:
        y_score = 0
        for person in p:
            if person in name:
                y_score += yearning[name.index(person)]
        result.append(y_score)
    
    return result
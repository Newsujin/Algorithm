
def solution(ingredient):
    ing = []
    cnt = 0
    
    for i in ingredient:
        ing.append(i)
        if ing[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del ing[-4:]
    
    return cnt
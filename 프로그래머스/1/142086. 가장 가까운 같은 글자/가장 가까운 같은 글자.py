def solution(s):
    answer = []
    dict = {}
    
    for index, word in enumerate(s):
        if word not in dict:
            answer.append(-1)
            dict[word] = index
    
        else:
            answer.append(index - dict[word])
            dict[word] = index
        
    return answer
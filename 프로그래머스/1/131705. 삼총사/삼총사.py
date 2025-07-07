def solution(number):
    answer = 0
    number_len = len(number)
    
    for i in range(number_len - 2):
        tmp = [number[i]]
        for j in range(i + 1, number_len - 1):
            tmp.append(number[j])
            for k in range(j + 1, number_len):
                tmp.append(number[k])
                if sum(tmp) == 0:
                    answer += 1
                tmp.pop()
            tmp.pop()
        tmp.pop()
        
    return answer
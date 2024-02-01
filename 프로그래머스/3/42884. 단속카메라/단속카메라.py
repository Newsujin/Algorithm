def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    camera = -30001
    answer = 0
    
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1

    return answer
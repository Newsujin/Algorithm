def solution(arr):
    lcm = max(arr)
    
    while True:
        divisor = 0
        for i in arr:
            if lcm % i == 0:
                divisor += 1
            else:
                break
        
        if divisor == len(arr):
            break
        lcm += 1
    
    return (lcm)
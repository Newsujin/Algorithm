from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
    numbers = list(numbers)
    number_set = set()
    cnt = 0
    
    for i in range(1, len(numbers) + 1):
        number_set |= set(map(int, map(''.join, permutations(numbers, i))))
    
    for num in number_set:
        if is_prime(num):
            cnt += 1
    
    return cnt

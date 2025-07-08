def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, a in enumerate(nums) :
        s = s.replace(a, str(i))
    
    return int(s)
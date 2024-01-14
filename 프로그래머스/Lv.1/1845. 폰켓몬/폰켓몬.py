def solution(nums):
    answer = set(nums)
    n = len(answer)
    if (n < len(nums) / 2):
        return (n)
    else:
        return len(nums) / 2
def solution(nums):
    hashDict = {}
    for n in nums:
        hashDict[hash(n)] = n
    
    hashLen = len(hashDict)
    numsLen = len(nums) // 2
    return (hashLen if hashLen < numsLen else numsLen)
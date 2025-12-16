def solution(nums):
    allow = len(nums)//2
    count = {}
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    answer = 0
    if len(count) > allow:
        answer = allow
    else:
        answer = len(count)
    return answer
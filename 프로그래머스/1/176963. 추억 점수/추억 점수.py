def solution(name, yearning, photo):
    answer = []
    dct = {}
    n = len(name)
    
    for i in range(n):
        dct[name[i]] = yearning[i]
    
    for memory in photo:
        count = 0
        for person in memory:
            if person in dct:
                count += dct[person]
        answer.append(count)    
    
    return answer
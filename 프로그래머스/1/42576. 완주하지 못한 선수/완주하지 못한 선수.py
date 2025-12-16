def solution(participant, completion):
    counter = {}
    
    for name in participant:
        counter[name] = counter.get(name, 0) + 1
    
    for name in completion:
        counter[name] -= 1
    
    for name, count in counter.items():
        if count > 0:
            return name
    
    return answer
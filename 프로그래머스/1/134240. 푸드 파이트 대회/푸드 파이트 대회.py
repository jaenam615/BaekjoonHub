from collections import deque

def solution(food):
    dq = deque([0])
    for i in range(len(food)-1, 0, -1):
        for j in range((food[i]//2)):
            dq.appendleft(i)
            dq.append(i)
    
    answer = list(dq)
    return ''.join(map(str, answer))
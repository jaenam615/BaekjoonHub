from collections import deque 

def isDiffByOne(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = []
    
    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            return steps
        
        for word in words:
            if word not in visited:
                if isDiffByOne(current, word):
                    visited.append(word)
                    queue.append((word, steps + 1))
        
    return 0
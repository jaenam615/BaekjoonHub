def solution(names, yearning, photos):
    answer = []
    score = 0
    
    for photo in photos:
        for name in names:
            if name in photo:
                score += yearning[names.index(name)]
        answer.append(score)
        score = 0
            
    return answer


def solution(make_id):
    
    check = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-','_','.']
    
    #1단계
    make_id = make_id.lower()

    
    #2단계
    new_id = ''
    for i in range(0, len(make_id)):
        if make_id[i] in check:
            new_id += make_id[i]
    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    #4단계
    if new_id and new_id[0] == '.': 
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    #5단계
    if len(new_id) == 0:
        new_id = 'a'
        
    #5단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    #6단계
    while new_id[-1] == '.':
        new_id = new_id[:-1]
    
    #7단계
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
        
    
    answer = new_id
    return answer
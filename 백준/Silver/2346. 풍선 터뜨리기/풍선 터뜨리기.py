# 백준 2346 풍선 터뜨리기
from collections import deque

N = int(input())
#enumerate는 인덱스와 같이 투플형태로 넣어준다.
dq = deque(enumerate(map(int, input().split()))) 
result = [] 

while dq:
    idx, number = dq.popleft()
    result.append(idx+1)
    #데크의 rotate 함수는 안에 들어있는 값만큼 회전한다. 
    #양수는 오른쪽으로, 음수면 왼쪽으로
    if number > 0:
        dq.rotate(-(number-1))
    else:
        dq.rotate(-number)
        
print(" ".join(map(str, result)))
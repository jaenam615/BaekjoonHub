import sys 
from collections import deque

N = input()

# Checker = (int(N[0]),int(N[1]))
set = deque()
value = -1
cycle = 0 

#입력값이 한자리수인지 두자리수인지 확인
if int(N) < 10:
    set.append(0)
    set.append(int(N))
    Checker = list(set)
else:
    set.append(int(N[0]))
    set.append(int(N[1]))
    Checker = list(set)

while True:
    
    #두 자리수의 값을 더한 값 구하기, popleft를 사용해서 먼저번 숫자의 두번째 자리 수 앞으로 땡김
    value = set.popleft() + set[0]
    #해당 값의 오른쪽 자리 수
    if value >= 10:
        ready = int(str(value)[1])
    else:
        ready = value 
    set.append(ready)
    cycle += 1
    if Checker[0] == set[0]:
        if Checker[1] == set[1]:
            break

print(cycle)
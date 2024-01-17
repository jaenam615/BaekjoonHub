N, L = map(int, input().split())
#False로 채워진 리스트를 만듬 (길이 1000까지 가도록)
coord = [False] * 1001

#입력한 값의 위치에 True로 바꿈 
for i in map(int,input().split()): 
    coord[i] = True

#테이프의 양
tape_amount = 0
#현재 위치 포인터
pointer = 0 

while pointer < 1001:
    #포인터의 위치에 구멍이 나있다면 
    if coord[pointer]:
        # 테이프를 하나 사용하고
        tape_amount += 1
        # 그 뒤에 테이프 길이 L 범위 내에 들어와 있을 수 있는 구멍은 가린 셈 치고 포인터를 L만큼 전진
        pointer += L
    else:
        pointer += 1

print(tape_amount)
import sys

N = int(sys.stdin.readline())
sold = dict()

for i in range(N):
    title = sys.stdin.readline().rstrip()
    if not title in sold:
        sold[title] = 1
    else:
        sold[title] += 1

most_amount = max(sold.values())  #sold라는 전체 판매 제목-수량 딕셔너리에서 최대로 팔린 수량 값 저장
most_title = []                   
for k, v in sold.items():         #sold 딕셔너리에 있는 키-값 페어에서
    if v == most_amount:          #값이 최대 수량인 항목들의 
        most_title.append(k)      #키값을 most_title이라는 리스트에 삽입

most_title.sort()                 #most_title을 정렬, 여기에는 키 값들만 있기 때문에 모두 문자열이다. 그럼으로 알파벳 순으로 정렬된다.

print(most_title[0])              #정렬 후에는 인덱스[0]에 가장 빠른 알파벳 순서가 오기 때문에 해당 키값을 출력한다.


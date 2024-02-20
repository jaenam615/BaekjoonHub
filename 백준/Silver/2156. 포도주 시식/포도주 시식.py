N = int(input())

wine = [0]  # 포도주 양을 저장할 리스트
for _ in range(N):
    wine.append(int(input()))

# 각 포도주 양을 마실 때의 최대 양을 저장할 리스트
max_drinking = [0 for _ in range(N + 1)]

# 초기값 설정
max_drinking[1] = wine[1]
if N > 1:
    max_drinking[2] = wine[1] + wine[2]

# 동적 프로그래밍을 통한 최대 양 계산
for i in range(3, N + 1):
    max_drinking[i] = max(
        max_drinking[i - 1],  # i번째 잔을 마시지 않는 경우
        max_drinking[i - 2] + wine[i],  # i번째 잔을 마시는 경우
        max_drinking[i - 3] + wine[i - 1] + wine[i]  # i-1번째와 i번째 잔을 연속해서 마시는 경우
    )

# 결과 출력
print(max_drinking[N])
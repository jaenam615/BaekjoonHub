def solution(triangle):
    height = len(triangle)
    cache = []

    # cache를 triangle과 같은 구조로 초기화
    for i in range(height):
        cache.append([0] * (i + 1))

    # 초기값 설정
    cache[0][0] = triangle[0][0]

    # DP로 cache 채우기
    for i in range(1, height):
        for j in range(len(triangle[i])):
            if j == 0:
                # 첫 번째 열
                cache[i][j] = cache[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                # 마지막 열
                cache[i][j] = cache[i-1][j-1] + triangle[i][j]
            else:
                # 중간 열
                cache[i][j] = max(cache[i-1][j-1], cache[i-1][j]) + triangle[i][j]

    answer = max(cache[-1])
    return answer
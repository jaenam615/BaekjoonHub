# 어떤 두 개를 없애야
# 최소 거리가 길어질까?
# 가장 비슷하게하게 나눠져있어야 할 것.
# 그러면, 길이가 25에 바위 다섯개중 두개 없애면 총 3개가 남으니까
# 가장 이상적인 것은 0, 5, 10, 15, 20 -> 최솟값 5
# 코드를 어떻게 짜야 저것과 근접하게 나올 것인가. 

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)  # 도착점도 검사에 포함

    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 목표 최소거리 d = mid

        removed = 0
        prev = 0  # 출발점

        for x in rocks:
            if x - prev < mid:
                removed += 1  # x를 제거
                if removed > n:
                    break
            else:
                prev = x  # x를 남김

        if removed <= n:     # mid(최소거리) 달성 가능
            answer = mid
            left = mid + 1   # 더 큰 최소거리도 가능한지
        else:                # mid 달성 불가능
            right = mid - 1

    return answer
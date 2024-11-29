def solution(n, m, section):
    count = 0
    i = 0  # section 리스트의 현재 인덱스

    while i < len(section):
        count += 1  # 페인트 횟수 증가
        start = section[i]  # 현재 구간의 시작점
        # 현재 시작점에서 m 길이만큼 덮기
        while i < len(section) and section[i] < start + m:
            i += 1  # 덮은 구간의 끝까지 진행

    return count

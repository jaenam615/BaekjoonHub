from collections import deque

def solution(priorities, location):
    dq = deque(
        (p, i == location)
        for i, p in enumerate(priorities)
    )

    answer = 0

    while dq:
        priority, is_target = dq.popleft()

        if dq and priority < max(p for p, _ in dq):
            dq.append((priority, is_target))
        else:
            answer += 1
            if is_target:
                return answer
from collections import deque

N, K = map(int, input().split())

order = deque(input().split())
multi = []
count = 0

# 사용할 전자기기가 남아 있는 동안
while order:
    now = order.popleft()
    # 사용하려는 것이 이미 꽂혀져 있다면 넘어가기
    if now in multi:
        continue

    # 멀티탭에 비어있는 구가 있다면 꽂아 쓰기
    if len(multi) < N:
        multi.append(now)
        continue

    order_idxs = []
    plugged = True

    for i in range(N):
        # 멀티탭에 꽂혀져 있는 것이 언젠가는 써야 한다면
        if multi[i] in order:
            # 언제 사용하는지 확인 (인덱스로)
            order_idx = order.index(multi[i])
        else:
            order_idx = 101
            plugged = False

        order_idxs.append(order_idx)

        if not plugged:
            continue

    # 가장 늦게 사용하는 녀석을
    unplug = order_idxs.index(max(order_idxs))
    del multi[unplug]
    multi.append(now)
    count += 1

print(count)

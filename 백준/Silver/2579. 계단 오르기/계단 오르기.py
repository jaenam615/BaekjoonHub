import sys

N = int(input())

stairs = []
stairs.append(0)

for _ in range(N):
    point = int(sys.stdin.readline())
    stairs.append(point)

max_points = [0] * (N + 1)
counter = 1

max_points[0] = 0
max_points[1] = stairs[1]


for i in range(2, len(stairs)):
    # if max_points[i] == max_points[i - 1] + max_points[i - 2]:
    #     max_points[i] = max_points[i - 2] + stairs[i]
    #     counter = 0
    max_points[i] = max(
        max_points[i - 3] + stairs[i] + stairs[i - 1], max_points[i - 2] + stairs[i]
    )

print(max_points[N])

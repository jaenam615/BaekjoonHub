import sys

N, P = map(int, sys.stdin.readline().split())

pressed = [[] for _ in range(6)]
movement = 0

for _ in range(N):
    string, fret = map(int, sys.stdin.readline().split())
    string -= 1

    if pressed[string] and pressed[string][-1] == fret:
        continue

    while pressed[string] and pressed[string][-1] > fret:
        pressed[string].pop()
        movement += 1

    if not pressed[string] or pressed[string][-1] < fret:
        pressed[string].append(fret)
        movement += 1

print(movement)
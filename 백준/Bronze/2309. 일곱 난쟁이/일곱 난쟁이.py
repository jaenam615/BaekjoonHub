from itertools import combinations

dwarves = []

for _ in range(9):
    dwarves.append(int(input()))

for i in combinations(dwarves, 7):
    if sum(i) == 100:
        order = sorted(i)
        for j in range(len(order)):
            print(order[j])
        break
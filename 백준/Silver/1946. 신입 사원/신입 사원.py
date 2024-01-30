import sys
T = int(input())


for i in range(T):
    people = []
    N = int(input())
    for j in range(N):
        R, I = map(int, sys.stdin.readline().split())
        people.append((R, I))
    people.sort()
    hired = people[0]
    count = 1
    v = 1
    for k in range(1,N):
        if people[k][1] < hired[1]:
            hired = people[k]
            count += 1
            v = k
    print(count)

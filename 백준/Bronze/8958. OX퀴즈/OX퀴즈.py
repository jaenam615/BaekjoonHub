T = int(input())

for _ in range(T):
    point = 0
    consec = 0
    result = input()
    for i in range(len(result)):
        if result[i] == 'O':
            consec += 1
            if (i+1) == len(result):
                point += (consec*(consec + 1))/2
        else:
            point += (consec*(consec + 1))/2
            consec = 0
    print(int(point))
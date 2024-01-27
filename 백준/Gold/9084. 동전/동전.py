T = int(input())

while T:
    N = int(input())
    K = list(map(int, input().split()))
    M = int(input())

    d = [0] * (M + 1)
    d[0] = 1

    for i in range(len(K)):
        for j in range(K[i], M + 1):
            d[j] += d[j - K[i]]

    print(d[M])
    T -= 1

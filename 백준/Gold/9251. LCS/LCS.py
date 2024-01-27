X = input()
Y = input()
X = "0" + X
Y = "1" + Y

cache = [[0] * (len(X)) for _ in range(len(Y))]

for i in range(1, len(Y)):
    for j in range(1, len(X)):
        if X[j] == Y[i]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

print(cache[len(Y) - 1][len(X) - 1])

import sys

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

MOD = 10007
cache = [[-1] * 1001 for _ in range(1001)]


def binomial(n, k):
    if cache[n][k] != -1:
        return cache[n][k]

    if k == 0 or n == k:
        cache[n][k] = 1
    else:
        cache[n][k] = binomial(n - 1, k - 1) + binomial(n - 1, k)

    return cache[n][k]


print(binomial(N, K) % MOD)

import sys

N = int(input())

MOD = 15746


cache = [0] * 1_000_001
cache[1] = 1
cache[2] = 2


for i in range(3, N + 1):
    cache[i] = (cache[i - 1] + cache[i - 2])%MOD

print(cache[N])

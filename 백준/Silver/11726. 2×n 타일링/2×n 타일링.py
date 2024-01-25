MOD = 10007

cache = [-1] * 1001
cache[1] = 1
cache[2] = 2

def tile(n):
    if cache[n] == -1:
        cache[n] = tile(n - 1) + tile(n - 2)
    return cache[n]


print(tile(int(input()))%MOD)

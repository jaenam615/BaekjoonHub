cache = [-1] * 91
cache[0] = 0
cache[1] = 1


def fibonacci(n):
    if cache[n] == -1:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]


print(fibonacci(int(input())))

N = int(input())


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ans = fib(n - 1) + fib(n - 2)
        return ans


print(fib(N))

import math

N , M = map(int, input().split())

def isPrime(n):
    if n ==1:
        return 0
    if n ==2:
        return 1
    for j in range(2,math.ceil(n**(1/2))+1):
        if n%j == 0:
            return 0
    return 1

for i in range(N, M+1):
    if isPrime(i):
        print(i)
    
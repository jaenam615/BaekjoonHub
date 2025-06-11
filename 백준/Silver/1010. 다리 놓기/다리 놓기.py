from sys import stdin
from math import factorial

def solution(N:int, M:int)-> int:
    ans = factorial(M)/(factorial(N) * factorial(M - N))

    return int(ans)
    

if __name__ == "__main__":
    T = int(input())

    for i in range(0, T):
        N, M = map(int, stdin.readline().split())
        print(solution(N, M))
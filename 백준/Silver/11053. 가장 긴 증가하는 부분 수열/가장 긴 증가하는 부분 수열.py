import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for i in range(1, N):
    for previous in range(i):
        if A[previous] < A[i]:
            if dp[previous] >= dp[i]:
                dp[i] = dp[previous] + 1

print(max(dp))

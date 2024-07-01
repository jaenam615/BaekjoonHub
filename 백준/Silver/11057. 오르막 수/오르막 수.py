import sys

input = sys.stdin.readline

N = int(input())

dp = list([0] * 10 for _ in range(N + 1))
dp[1] = [1] * 10

for k in range(N + 1):
    dp[k][0] = 1

for i in range(2, N + 1):
    for j in range(10):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(sum(dp[N]) % 10007)

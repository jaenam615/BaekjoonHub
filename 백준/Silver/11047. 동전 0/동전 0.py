import sys

N, K = map(int, sys.stdin.readline().split())

A = [int(sys.stdin.readline()) for _ in range(N)]
A.reverse()
total_coins =0

for i in range(len(A)):    
    if A[i] <= K:
        amount = K//A[i]
        total_coins += amount
        K -= (A[i]*amount)
    else:
        continue
    if K == 0:
        break

print(total_coins)
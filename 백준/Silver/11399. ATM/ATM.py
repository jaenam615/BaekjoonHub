N = int(input())

time = list(map(int, input().split()))

time.sort()

def solution():
    sum = 0
    for i in range(N):
        sum += time[i] * (N - i)
    return sum

print(solution())
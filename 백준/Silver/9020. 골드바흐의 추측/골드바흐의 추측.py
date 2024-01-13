import sys
N = int(input())
a = [sys.stdin.readline() for j in range(N)]

def isSosu(num):
    result = False
    count = 0
    for i in range(1, int(num ** 0.5)+1):
        if num % i == 0:
            count += 1
    if count == 1:
        return True
    return result


for i in a:
    num = int(i)//2
    while True:
        if isSosu(num) & isSosu(int(i)-num):
            print(num,int(i)-num)
            break
        num -= 1
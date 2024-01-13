import sys

a = int(sys.stdin.readline())


def hanoi(n, A, B, C):
    if n == 1:
        print (A, B)
        return
    else:
        hanoi(n-1, A,C,B)
        print (A, B)
        hanoi(n-1, C,B,A) 

print((-1)*(1-(2**a)))
if a <= 20:
    hanoi(a, 1,3,2)
import sys

T = int(sys.stdin.readline())
s = []

for _ in range(T):
    VPS = True    
    A = input()
    s.clear()
    for j in range(len(A)):
        if A[j] == "(":
            s.append(A[j])
        else:
            if len(s) > 0:
                s.pop()
            else:
                VPS = False
                break
    if len(s) > 0:
        VPS = False
    if VPS == True:
        print("YES")
    else:
        print("NO")

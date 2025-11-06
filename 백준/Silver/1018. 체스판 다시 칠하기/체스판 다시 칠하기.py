import sys

N, M = map(int, sys.stdin.readline().split())
board = []
ans = 32

for _ in range(N):
    board.append(sys.stdin.readline().strip())

def fill(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2:
                if board[y+i][x+j] == bw:
                    cnt +=1
            else:
                if board[y+i][x+j] != bw:
                    cnt +=1
    ans = min(cnt, ans)

for i in range(0, N-7):
    for j in range(0, M-7):
        fill(i, j, 'B')
        fill(i, j, 'W')

print(ans)
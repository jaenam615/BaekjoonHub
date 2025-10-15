from sys import stdin

#king / queen / rook / bishop / knight / pawn

def solution(p: list[int], c: list[int]) -> list[int]:
    return [correct[i] - pieces[i] for i in range(len(pieces))]

pieces = list(map(int, stdin.readline().split()))
correct = [1, 1, 2, 2, 2, 8]

print(*solution(pieces, correct))
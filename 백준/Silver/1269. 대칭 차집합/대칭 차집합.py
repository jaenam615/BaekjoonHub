import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = set(map(int, input().rstrip().split()))
B = set(map(int, input().rstrip().split()))

print(len(A-B) + len(B-A))
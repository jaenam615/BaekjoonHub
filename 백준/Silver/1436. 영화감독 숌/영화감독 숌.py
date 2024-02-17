import sys

N = int(input())
start = 665
counter = 0

while(True):
    if "666" in str(start):
        counter += 1
        if counter == N:
            print(start)
            break
    start += 1
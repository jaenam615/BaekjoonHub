import sys

N = int(sys.stdin.readline())
words = set()
sorted_words =[]
i = 0


while i < N:
    w = sys.stdin.readline()
    words.add(w.strip())
    i += 1

sorted_words = sorted(words)
sorted_words.sort(key=len)

for word in sorted_words:
    print(word)

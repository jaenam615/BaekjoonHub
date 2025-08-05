import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]

letter_weights = {}

for word in words:
    for i, letter in enumerate(reversed(word)):
        place_value = 10**i
        letter_weights[letter] = letter_weights.get(letter, 0) + place_value

sorted_letters = sorted(letter_weights.keys(), key=lambda l: letter_weights[l], reverse=True)

letter_num_map = {}
current_num = 9
for letter in sorted_letters:
    letter_num_map[letter] = current_num
    current_num -= 1

total_sum = 0
for word in words:
    word_value_str = ""
    for letter in word:
        word_value_str += str(letter_num_map[letter])
    total_sum += int(word_value_str)

print(total_sum)
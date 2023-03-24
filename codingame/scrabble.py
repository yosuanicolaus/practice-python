import sys
import math

points = {}
available = {}
dictionary: dict[str, dict[str, int]] = {}
best = 0
best_word = ""

# initialize points (from scrabble rules)
for ch in 'eaionrtlsu':
    points[ch] = 1
points['d'] = points['g'] = 2
for ch in 'bcmp':
    points[ch] = 3
for ch in 'fhvwy':
    points[ch] = 4
points['k'] = 5
points['j'] = points['x'] = 8
points['q'] = points['z'] = 10

# get input
n = int(input())
for i in range(n):
    w = input()
    word_dict = {}
    for ch in w:
        word_dict[ch] = 1 + word_dict.get(ch, 0)
    dictionary[w] = word_dict
letters = input()
for ch in letters:
    available[ch] = 1 + available.get(ch, 0)

# for each word dictionary, check if eligible, while counting points
for word, word_dict in dictionary.items():
    count = 0
    for ch in word_dict:
        if ch not in available or available[ch] < word_dict[ch]:
            break
        count += points[ch]
    else:
        if count > best:
            best = count
            best_word = word

print(best_word)

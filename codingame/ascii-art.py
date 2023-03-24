import sys
import math
import string

'''
first, get the ascii source and save in a array
allocate a result 2d array (of char) with the correct height and length with ' ' default val
loop over the text and our result arr at the same time, write the ascii on res
'''

ascii_dict = []

l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()
    ascii_dict.append(list(row))

result = [[" " for _ in range(l*len(t))] for _ in range(h)]


for i, ch in enumerate(t):
    if ch in string.ascii_lowercase:
        ch = ch.upper()
    cdi = (ord(ch) - ord('A')) * l
    if ch not in string.ascii_letters:
        cdi = 26 * l
    dcdi = cdi

    for r in range(h):
        for c in range(i*l, i*l+l):
            result[r][c] = ascii_dict[r][cdi]
            cdi += 1
        cdi = dcdi


for list_res in result:
    print(''.join(list_res))

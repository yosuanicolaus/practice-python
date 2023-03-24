import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

field = []
check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

w = int(input())
h = int(input())
for i in range(h):
    line = input()
    field.append(list(line))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for y in range(h):
    for x in range(w):
        if field[y][x] == 'x':
            for ay, ax in check:
                cy, cx = y + ay, x + ax
                if not (0 <= cy < h and 0 <= cx < w) or \
                        field[cy][cx] == 'x':
                    continue
                elif field[cy][cx] == '.':
                    field[cy][cx] = '1'
                else:
                    field[cy][cx] = str(int(field[cy][cx]) + 1)

# sanitize all mine
for y in range(h):
    for x in range(w):
        if field[y][x] == 'x':
            field[y][x] = '.'

for linelist in field:
    print(''.join(linelist))

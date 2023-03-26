import sys
import math

# Don't let the machines win. You are humanity's last hope...
cells = []

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    cells.append(line)


for r in range(height):
    for c in range(width):
        if cells[r][c] == '.':
            continue
        y1, x1 = r, c
        y2, x2 = -1, -1
        y3, x3 = -1, -1

        # search right
        for nc in range(c+1, width):
            if cells[r][nc] == '0':
                y2, x2 = r, nc
                break

        # search down
        for nr in range(r+1, height):
            if cells[nr][c] == '0':
                y3, x3 = nr, c
                break

        print(x1, y1, x2, y2, x3, y3)
